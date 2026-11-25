"""The VaniDesk web app: a health check and the owner dashboard."""

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import create_tables, get_db
from app.db.models import Appointment, CallLog
from app.sample_data import BUSINESS

app = FastAPI(title="VaniDesk")

# The folder that holds index.html. It is looked up from the folder you start
# uvicorn in, so always start uvicorn from the top folder of the project.
templates = Jinja2Templates(directory="dashboard")

# Make sure the tables exist, so the page works even before seed.py has run.
create_tables()


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


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def home():
    """Send anyone who opens the bare address to the dashboard."""
    return RedirectResponse(url="/dashboard")


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
