"""add users

Revision ID: 2bd7bbd2736e
Revises: 657c25b46780
Create Date: 2024-10-08 18:53:25.321365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table
from app.core.security import get_password_hash

# revision identifiers, used by Alembic.
revision: str = '2bd7bbd2736e'
down_revision: Union[str, None] = '657c25b46780'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_table = table("users",
                       sa.Column('id', sa.Integer(), nullable=False),
                       sa.Column('username', sa.String(), nullable=True),
                       sa.Column('hashed_password', sa.String(), nullable=True),
                       sa.Column('role', sa.String(), nullable=True)
                       )
    op.bulk_insert(user_table,
                   [
                       {"username": "user",
                        "hashed_password": get_password_hash("L0XuwPOdS5U"),
                        "role": "user"},
                       {"username": "admin",
                        "hashed_password": get_password_hash("JKSipm0YH"),
                        "role": "admin"},
                   ]
                   )


def downgrade() -> None:
    pass
