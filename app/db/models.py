"""The two tables the dashboard reads: calls and appointments."""

from datetime import datetime

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class CallLog(Base):
    """One phone call that VaniDesk answered."""

    __tablename__ = "call_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    caller_number: Mapped[str]
    language: Mapped[str]
    # Date and time in the business's local time. No time zone is stored.
    started_at: Mapped[datetime]
    duration_seconds: Mapped[int]
    # What VaniDesk did on the call, one sentence per line.
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
