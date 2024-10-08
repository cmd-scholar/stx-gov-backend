"""Add total_votes column to proposals

Revision ID: 658bb0cd9a0d
Revises: a03ef59aa9a1
Create Date: 2024-09-19 02:21:29.075954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '658bb0cd9a0d'
down_revision: Union[str, None] = 'a03ef59aa9a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proposals', sa.Column('total_votes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proposals', 'total_votes')
    # ### end Alembic commands ###