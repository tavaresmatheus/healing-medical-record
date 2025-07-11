from datetime import datetime, timezone
import uuid
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
from app.models.user import User

class Doctor(SQLModel, table=True):
    __tablename__ = 'doctors'

    doctor_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key='users.user_id')
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime

    user: Optional[User] = Relationship(back_populates='doctors')
