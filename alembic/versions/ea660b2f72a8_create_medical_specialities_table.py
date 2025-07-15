"""create medical_specialities table

Revision ID: ea660b2f72a8
Revises: 7144e01ee2e3
Create Date: 2025-07-15 18:34:52.679360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea660b2f72a8'
down_revision: Union[str, Sequence[str], None] = '7144e01ee2e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'medical_specialities',
        sa.Column('medical_speciality_id', sa.Uuid, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True)
        )


def downgrade() -> None:
    op.drop_table('medical_specialities')
