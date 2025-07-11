import uuid
from sqlmodel import Field, SQLModel

class MedicalSpeciality(SQLModel, table=True):
    __tablename__ = 'medical_specialities'

    medical_speciality_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=255)
