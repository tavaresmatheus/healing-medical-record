import uuid

from sqlmodel import SQLModel, Field
from datetime import datetime, timezone, date
from typing import Optional

class User(SQLModel, table=True):
    __tablename__ = 'users'

    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=255)
    email: str = Field(max_length=255, unique=True)
    birth_date: date
    cpf: str = Field(max_length=11, unique=True)
    rg: str = Field(max_length=9, unique=True)
    email_verified: Optional[datetime] = None
    password: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime
