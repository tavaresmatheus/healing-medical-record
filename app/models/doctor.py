import uuid
from datetime import datetime, timezone
from typing import List
from sqlmodel import Field, SQLModel, Relationship

class Doctor(SQLModel, table=True):
    __tablename__ = 'doctors'

    doctor_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key='users.user_id', unique=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime

    user: 'User' = Relationship(back_populates='doctor')
    doctor_medical_specialities: List['DoctorMedicalSpeciality'] = Relationship(back_populates='doctor')
    doctor_crms: List['DoctorCrm'] = Relationship(back_populates='doctor')
