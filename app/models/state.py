from datetime import datetime, timezone
import uuid
from sqlmodel import Field, SQLModel

class State(SQLModel, table=True):
    __tablename__ = 'states'

    state_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    state: str = Field(max_length=255)
    uf: str = Field(max_length=2)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime
