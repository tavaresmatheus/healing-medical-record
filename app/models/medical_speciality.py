import uuid
from datetime import datetime, timezone
from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship

class MedicalSpeciality(SQLModel, table=True):
    __tablename__ = 'medical_specialities'

    medical_speciality_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime

    doctor_medical_specialities: List['DoctorMedicalSpeciality'] = Relationship(back_populates='medical_speciality')
