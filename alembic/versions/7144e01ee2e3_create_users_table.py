"""create users table

Revision ID: 7144e01ee2e3
Revises: 
Create Date: 2025-07-15 18:03:02.183519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7144e01ee2e3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_id', sa.Uuid, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('birth_date', sa.Date, nullable=False),
        sa.Column('cpf', sa.String(11), nullable=False, unique=True),
        sa.Column('rg', sa.String(9), nullable=False, unique=True),
        sa.Column('email_verified', sa.Boolean, default=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True)
        )


def downgrade() -> None:
    op.drop_table('users')
