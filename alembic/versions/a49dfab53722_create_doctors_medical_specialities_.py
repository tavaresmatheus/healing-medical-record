"""create doctors_medical_specialities table

Revision ID: a49dfab53722
Revises: aeff2fd49058
Create Date: 2025-07-15 19:00:06.918684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a49dfab53722'
down_revision: Union[str, Sequence[str], None] = 'aeff2fd49058'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'doctors_medical_specialities',
        sa.Column('doctor_medical_speciality_id', sa.Uuid, primary_key=True),
        sa.Column('doctor_id', sa.Uuid, sa.ForeignKey('doctors.doctor_id'), nullable=False),
        sa.Column('medical_speciality_id', sa.Uuid, sa.ForeignKey('medical_specialities.medical_speciality_id]'), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True)
        )


def downgrade() -> None:
    op.drop_table('doctors_medical_specialities')
