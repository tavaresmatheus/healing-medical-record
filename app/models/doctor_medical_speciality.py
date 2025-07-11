import uuid
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.models.doctor import Doctor
from app.models.medical_speciality import MedicalSpeciality

class DoctorMedicalSpeciality(SQLModel, table=True):
    __tablename__ = 'doctors_medical_specialities'

    doctor_medical_speciality_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    doctor_id: uuid.UUID = Field(foreign_key='doctors.doctor_id')
    medical_speciality_id: uuid.UUID = Field(foreign_key='medical_specialities.medical_speciality_id')

    doctor: Optional[Doctor] = Relationship(back_populates='doctors')
    medical_speciality: Optional[MedicalSpeciality] = Relationship(back_populates='medical_specialities')
