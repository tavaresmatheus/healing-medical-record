import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel, Text

from app.models.user import User

class MedicalRecord(SQLModel, table=True):
    __tablename__ = 'medical_records'

    medical_record_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    medical_record: str = Field(sa_column=Text)
    user_id: uuid.UUID = Field(foreign_key='users.user_id')
    doctor_id: uuid.UUID = Field(foreign_key='doctors.doctor_id')
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime

    user: Optional[User] = Relationship(back_populates='medical_records')
    doctor: Optional["Doctor"] = Relationship(back_populates="medical_records")
