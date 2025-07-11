import uuid

from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from app.models.doctor import Doctor
from app.models.state import State


class DoctorCrm(SQLModel, table=True):
    __tablename__ = 'doctors_crms'

    doctor_crm_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    doctor_id: uuid.UUID = Field(foreign_key='doctors.doctor_id')
    state_id: uuid.UUID = Field(foreign_key='states.state_id')
    crm: str = Field(max_length=6)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime

    doctor: Optional[Doctor] = Relationship(back_populates='doctors')
    state: Optional[State] = Relationship(back_populates='states')
