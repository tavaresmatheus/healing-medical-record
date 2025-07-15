"""create states table

Revision ID: 40921b223301
Revises: 37058a307ca0
Create Date: 2025-07-15 18:50:51.653939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40921b223301'
down_revision: Union[str, Sequence[str], None] = '37058a307ca0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'states',
        sa.Column('state_id', sa.Uuid, primary_key=True),
        sa.Column('state', sa.String(255), nullable=False, unique=True),
        sa.Column('uf', sa.String(2), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True)
        )

def downgrade() -> None:
    op.drop_column('states')
