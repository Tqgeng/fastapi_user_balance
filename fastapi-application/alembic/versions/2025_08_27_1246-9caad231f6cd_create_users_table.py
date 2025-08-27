"""create users table

Revision ID: 9caad231f6cd
Revises: a64a5c0c7658
Create Date: 2025-08-27 12:46:38.343681

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9caad231f6cd"
down_revision: Union[str, Sequence[str], None] = "a64a5c0c7658"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("balance", sa.Integer(), nullable=False))


def downgrade() -> None:
    op.drop_column("users", "balance")
