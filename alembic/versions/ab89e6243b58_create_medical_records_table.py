"""create medical_records table

Revision ID: ab89e6243b58
Revises: a49dfab53722
Create Date: 2025-07-15 19:03:15.209341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab89e6243b58'
down_revision: Union[str, Sequence[str], None] = 'a49dfab53722'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'medical_records',
        sa.Column('medical_record_id', sa.Uuid, primary_key=True),
        sa.Column('user_id', sa.Uuid, sa.ForeignKey('users.user_id'), nullable=False),
        sa.Column('doctor_id', sa.Uuid, sa.ForeignKey('doctors.doctor_id'), nullable=False),
        sa.Column('medical_history', sa.Text, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True)
    )

def downgrade() -> None:
    op.drop_table('medical_records')