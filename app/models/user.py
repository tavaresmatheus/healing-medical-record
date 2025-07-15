import uuid
from datetime import datetime, timezone, date
from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship

class User(SQLModel, table=True):
    __tablename__ = 'users'

    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str
    birth_date: date
    cpf: str
    rg: str
    email_verified: bool = Field(default=False)
    password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default=None)

    doctor: Optional['Doctor'] = Relationship(back_populates='user')
    medical_records: List['MedicalRecord'] = Relationship(back_populates='user')
