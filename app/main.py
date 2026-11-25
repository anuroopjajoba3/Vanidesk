"""The web app: the public website pages, a health check and the owner dashboard."""

import os
import sys
from pathlib import Path

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import settings
from app.db.database import create_tables, get_db
from app.db.models import Appointment, CallLog, DemoRequest
from app.sample_data import BUSINESS

app = FastAPI(title=settings.app_name)

# The two folders that hold the HTML files. "website" has the public pages
# (home, pricing and so on) and "dashboard" has index.html, the owner dashboard.
# A full path is used so the pages still load when the app is not started
# from the project folder, which is how Vercel starts it.
ROOT = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=[str(ROOT / "website"), str(ROOT / "dashboard")])

# Let every HTML file write {{ app_name }}. The name itself is written in one
# place only: app/config.py.
templates.env.globals["app_name"] = settings.app_name

# Make sure the tables exist, so the pages work even before seed.py has run.
create_tables()

# Vercel starts with an empty database. Fill it with the sample calls so the
# dashboard is not blank. seed() does nothing when calls are already there.
if os.environ.get("VERCEL"):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from seed import seed

    seed()


def format_duration(seconds):
    """Turn 134 into "2m 14s"."""
    minutes = seconds // 60
    seconds_left = seconds % 60
    return f"{minutes}m {seconds_left}s"


def make_summary_line(appointments):
    """Build the line above the table, such as "Done. 1 booked, 1 cancelled:"."""
    if not appointments:
        return "Done. No appointment was booked or changed on this call."

    confirmed = 0
    pending = 0
    cancelled = 0
    for appointment in appointments:
        if appointment.status == "Confirmed":
            confirmed += 1
        elif appointment.status == "Pending":
            pending += 1
        else:
            cancelled += 1

    parts = []
    if confirmed > 0:
        parts.append(f"{confirmed} booked")
    if pending > 0:
        parts.append(f"{pending} waiting for your OK")
    if cancelled > 0:
        parts.append(f"{cancelled} cancelled")

    return "Done. " + ", ".join(parts) + ":"


def looks_like_email(text):
    """A simple check: no spaces, one @ with something before it, and a dot after it.

    "priya@example.com" passes. "priya", "priya@" and "priya@example" do not.
    """
    if " " in text or text.count("@") != 1:
        return False
    before_at, after_at = text.split("@")
    if before_at == "":
        return False
    return "." in after_at.strip(".")


@app.get("/health")
def health():
    return {"status": "ok"}


# ============ The public website ============
# Each route below shows one HTML file from the "website" folder.
# Every one of those files extends website/base.html, the shared layout.


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")


@app.get("/how-it-works", response_class=HTMLResponse)
def how_it_works(request: Request):
    return templates.TemplateResponse(request=request, name="how-it-works.html")


@app.get("/pricing", response_class=HTMLResponse)
def pricing(request: Request):
    return templates.TemplateResponse(request=request, name="pricing.html")


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(request=request, name="about.html")


@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    """The login screen. It is only a screen for now: the form does not log anyone in."""
    return templates.TemplateResponse(request=request, name="login.html")


@app.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    """The sign-up screen. It is only a screen for now: the form does not create accounts."""
    return templates.TemplateResponse(request=request, name="signup.html")


@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    """Show the empty Contact / Book a demo form."""
    # After a request is saved, the browser is sent to /contact?sent=1,
    # and the page shows a thank-you message instead of the form.
    sent = request.query_params.get("sent") == "1"

    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={"sent": sent, "errors": [], "form": {}},
    )


@app.post("/contact", response_class=HTMLResponse)
def contact_submit(
    request: Request,
    # Form("") reads a box of the form by its name. A box that was left out is "".
    name: str = Form(""),
    email: str = Form(""),
    business_name: str = Form(""),
    phone: str = Form(""),
    message: str = Form(""),
    db: Session = Depends(get_db),
):
    """Check what was typed into the form, and save it as one DemoRequest row."""
    # strip() removes spaces at the start and the end.
    form = {
        "name": name.strip(),
        "email": email.strip(),
        "business_name": business_name.strip(),
        "phone": phone.strip(),
        "message": message.strip(),
    }

    errors = []
    if form["name"] == "":
        errors.append("Please enter your name.")
    if form["email"] == "":
        errors.append("Please enter your email address.")
    elif not looks_like_email(form["email"]):
        errors.append("That email address does not look right. It should look like name@example.com.")

    # The boxes in the HTML have the same limits (maxlength). This second check
    # is here because a request can also be sent without using the page.
    if len(form["name"]) > 100:
        errors.append("Please keep your name under 100 characters.")
    if len(form["email"]) > 200:
        errors.append("Please keep your email address under 200 characters.")
    if len(form["business_name"]) > 150:
        errors.append("Please keep the business name under 150 characters.")
    if len(form["phone"]) > 30:
        errors.append("Please keep the phone number under 30 characters.")
    if len(form["message"]) > 2000:
        errors.append("Please keep your message under 2000 characters.")

    if errors:
        # Show the form again with the messages, and keep what was typed.
        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context={"sent": False, "errors": errors, "form": form},
            status_code=400,
        )

    demo_request = DemoRequest(
        name=form["name"],
        email=form["email"],
        business_name=form["business_name"],
        phone=form["phone"],
        message=form["message"],
    )
    db.add(demo_request)
    db.commit()

    # Send the browser to a normal page instead of answering the POST directly.
    # That way, refreshing the thank-you page cannot save the request twice.
    return RedirectResponse(url="/contact?sent=1", status_code=303)


# ============ The owner dashboard ============


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(
    request: Request,
    call_id: int | None = None,
    db: Session = Depends(get_db),
):
    # The ten newest calls, for the "Recent calls" list.
    ten_newest = select(CallLog).order_by(CallLog.started_at.desc()).limit(10)
    recent_calls = db.execute(ten_newest).scalars().all()

    # Which call to show: the one named in the address (?call_id=3),
    # or the newest one when the address names none.
    if call_id is None:
        newest = select(CallLog).order_by(CallLog.started_at.desc()).limit(1)
        call = db.execute(newest).scalars().first()
    else:
        call = db.get(CallLog, call_id)
        if call is None:
            raise HTTPException(status_code=404)

    # With an empty database there is no call at all, so these stay empty.
    appointments = []
    steps = []
    duration = ""
    summary_line = ""

    if call is not None:
        appointments = db.execute(
            select(Appointment)
            .where(Appointment.call_id == call.id)
            .order_by(Appointment.id)
        ).scalars().all()
        steps = call.summary.splitlines()
        duration = format_duration(call.duration_seconds)
        summary_line = make_summary_line(appointments)

    # Every appointment from every call, soonest first, for the Appointments view.
    all_appointments = db.execute(
        select(Appointment).order_by(Appointment.starts_at)
    ).scalars().all()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "business": BUSINESS,
            "call": call,
            "steps": steps,
            "duration": duration,
            "summary_line": summary_line,
            "appointments": appointments,
            "recent_calls": recent_calls,
            "all_appointments": all_appointments,
        },
    )
