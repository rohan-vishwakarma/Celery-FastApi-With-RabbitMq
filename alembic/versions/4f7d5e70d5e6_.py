"""empty message

Revision ID: 4f7d5e70d5e6
Revises: dd67a562be0a
Create Date: 2024-03-25 00:04:49.475332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f7d5e70d5e6'
down_revision: Union[str, None] = 'dd67a562be0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    pass


def downgrade() -> None:
    pass
