"""Fill the database with the sample calls from app/sample_data.py.

Run it once from the top folder:

    python seed.py

To start again from scratch, delete the database file (receptionist.db) and run it again.
"""

from sqlalchemy import func, select

from app.config import settings
from app.db.database import SessionLocal, create_tables
from app.db.models import Appointment, CallLog
from app.sample_data import SAMPLE_CALLS


def seed():
    create_tables()
    db = SessionLocal()

    calls_in_database = db.execute(select(func.count(CallLog.id))).scalar()
    if calls_in_database > 0:
        print(f"The database already has {calls_in_database} calls. Nothing was added.")
        # Take the file name out of the setting: "sqlite:///./receptionist.db"
        # becomes "./receptionist.db". That way the message names the real file.
        database_file = settings.database_url.replace("sqlite:///", "")
        print(f"To start again, delete the file {database_file} and run this script again.")
        db.close()
        return

    appointment_count = 0

    for sample in SAMPLE_CALLS:
        call = CallLog(
            caller_number=sample["caller_number"],
            language=sample["language"],
            started_at=sample["started_at"],
            duration_seconds=sample["duration_seconds"],
            # The sample data keeps one sentence per list item.
            # The database keeps them as one text, one sentence per line.
            summary="\n".join(sample["summary"]),
            transcript="\n".join(sample["transcript"]),
            sms_sent=sample["sms_sent"],
        )
        db.add(call)
        # commit() saves the call and gives it an id, which the appointments need.
        db.commit()

        for sample_appointment in sample["appointments"]:
            appointment = Appointment(
                call_id=call.id,
                customer_name=sample_appointment["customer_name"],
                service=sample_appointment["service"],
                starts_at=sample_appointment["starts_at"],
                status=sample_appointment["status"],
            )
            db.add(appointment)
            appointment_count += 1
        db.commit()

    db.close()
    print(f"Added {len(SAMPLE_CALLS)} calls and {appointment_count} appointments.")


if __name__ == "__main__":
    seed()
