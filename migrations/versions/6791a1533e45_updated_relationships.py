"""updated relationships

Revision ID: 6791a1533e45
Revises: 7a3ae83be8af
Create Date: 2024-09-19 18:58:23.548945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '6791a1533e45'
down_revision: Union[str, None] = '7a3ae83be8af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proposals', sa.Column('created_by_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(None, 'proposals', 'users', ['created_by_id'], ['uuid'])
    op.drop_column('proposals', 'created_by')
    op.add_column('votes', sa.Column('created_by_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(None, 'votes', 'users', ['created_by_id'], ['uuid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.drop_column('votes', 'created_by_id')
    op.add_column('proposals', sa.Column('created_by', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'proposals', type_='foreignkey')
    op.drop_column('proposals', 'created_by_id')
    # ### end Alembic commands ###