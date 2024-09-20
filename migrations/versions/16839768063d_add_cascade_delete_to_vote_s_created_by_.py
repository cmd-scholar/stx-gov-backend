"""Add cascade delete to Vote's created_by_id foreign key

Revision ID: 16839768063d
Revises: e176beb03c22
Create Date: 2024-09-20 02:55:25.183481

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '16839768063d'
down_revision: Union[str, None] = 'e176beb03c22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_votes_created_by_id_users', 'votes', type_='foreignkey')
    op.create_foreign_key(None, 'votes', 'users', ['created_by_id'], ['uuid'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.create_foreign_key('fk_votes_created_by_id_users', 'votes', 'users', ['created_by_id'], ['uuid'])
    # ### end Alembic commands ###