"""create doctors_crms table

Revision ID: aeff2fd49058
Revises: 40921b223301
Create Date: 2025-07-15 18:54:48.494200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aeff2fd49058'
down_revision: Union[str, Sequence[str], None] = '40921b223301'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'doctors_crms',
        sa.Column('doctor_crm_id', sa.Uuid, primary_key=True),
        sa.Column('doctor_id', sa.Uuid, sa.ForeignKey('doctors.doctor_id'), nullable=False),
        sa.Column('state_id', sa.Uuid, sa.ForeignKey('states.state_id'), nullable=False),
        sa.Column('crm', sa.String(6), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True)
        )


def downgrade() -> None:
    op.drop_table('doctors_crms')
