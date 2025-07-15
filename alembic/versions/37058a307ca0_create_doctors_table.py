"""create doctors table

Revision ID: 37058a307ca0
Revises: ea660b2f72a8
Create Date: 2025-07-15 18:37:48.129983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37058a307ca0'
down_revision: Union[str, Sequence[str], None] = 'ea660b2f72a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'doctors',
        sa.Column('doctor_id', sa.Uuid, primary_key=True),
        sa.Column('user_id', sa.Uuid, sa.ForeignKey('users.user_id'), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True)
        )


def downgrade() -> None:
    op.drop_table('doctors')
