
"""Table medical_records {
  medical_record_id integer [primary key]
  medical_history text [not null]
  user_id integer [ref: - users.user_id]
}"""

from typing import Optional
import uuid
from sqlmodel import Field, Relationship, SQLModel, Text

from app.models.user import User


class MedicalRecord(SQLModel, table=True):
    __tablename__ = 'medical_records'

    medical_record_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    medical_record: str = Field(sa_column=Text)
    user_id: uuid.UUID = Field(foreign_key='users.user_id')

    user: Optional[User] = Relationship(back_populates='users')
