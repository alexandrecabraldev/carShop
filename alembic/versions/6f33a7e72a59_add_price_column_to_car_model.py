"""Add price column to Car model

Revision ID: 6f33a7e72a59
Revises: 51e59364c95c
Create Date: 2024-05-31 14:35:19.758323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f33a7e72a59'
down_revision: Union[str, None] = '51e59364c95c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('price', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cars', 'price')
    # ### end Alembic commands ###
