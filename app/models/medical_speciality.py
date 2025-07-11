import uuid
from datetime import datetime, timezone

from sqlmodel import Field, SQLModel

class MedicalSpeciality(SQLModel, table=True):
    __tablename__ = 'medical_specialities'

    medical_speciality_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime
