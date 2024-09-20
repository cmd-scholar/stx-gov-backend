"""Add cascade delete to Proposal's created_by_id foreign key

Revision ID: e176beb03c22
Revises: a469f6574234
Create Date: 2024-09-20 02:53:21.722780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'e176beb03c22'
down_revision: Union[str, None] = 'a469f6574234'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_proposals_created_by_id_users', 'proposals', type_='foreignkey')
    op.create_foreign_key(None, 'proposals', 'users', ['created_by_id'], ['uuid'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'proposals', type_='foreignkey')
    op.create_foreign_key('fk_proposals_created_by_id_users', 'proposals', 'users', ['created_by_id'], ['uuid'])
    # ### end Alembic commands ###