"""create user table

Revision ID: 3d3f96782244
Revises: 
Create Date: 2024-03-25 11:10:12.571919

"""
import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d3f96782244'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('hashed_password', sa.String(200)),
        sa.Column('is_active', sa.Boolean()),
        sa.Column("datetime", sa.DATETIME(datetime.datetime.utcnow()))

    )
def downgrade() -> None:
    pass
