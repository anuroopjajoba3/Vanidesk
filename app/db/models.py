"""The tables: calls and appointments for the dashboard, and demo requests
from the contact form on the website."""

from datetime import datetime

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class CallLog(Base):
    """One phone call that the receptionist answered."""

    __tablename__ = "call_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    caller_number: Mapped[str]
    language: Mapped[str]
    # Date and time in the business's local time. No time zone is stored.
    started_at: Mapped[datetime]
    duration_seconds: Mapped[int]
    # What the receptionist did on the call, one sentence per line.
    summary: Mapped[str] = mapped_column(Text)
    transcript: Mapped[str] = mapped_column(Text)
    # True when a confirmation text went to the caller.
    sms_sent: Mapped[bool] = mapped_column(default=False)


class Appointment(Base):
    """One appointment that was booked, requested or cancelled on a call."""

    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(primary_key=True)
    # Which call this appointment came from.
    call_id: Mapped[int] = mapped_column(ForeignKey("call_logs.id"))
    customer_name: Mapped[str]
    service: Mapped[str]
    starts_at: Mapped[datetime]
    # "Confirmed", "Pending" or "Cancelled"
    status: Mapped[str]


class DemoRequest(Base):
    """One message sent with the form on the Contact / Book a demo page."""

    __tablename__ = "demo_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    # These three are optional on the form. An empty box is saved as "".
    business_name: Mapped[str]
    phone: Mapped[str]
    message: Mapped[str] = mapped_column(Text)
    # When the form was sent: the date and time on the computer that runs the app.
    # default=datetime.now fills it in by itself each time a row is added.
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
