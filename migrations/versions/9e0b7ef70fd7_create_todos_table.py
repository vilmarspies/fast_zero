"""create todos table

Revision ID: 9e0b7ef70fd7
Revises: bd5a39b5d0b8
Create Date: 2024-06-03 13:56:07.046767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e0b7ef70fd7'
down_revision: Union[str, None] = 'bd5a39b5d0b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    op.add_column('todos', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'updated_at')
    op.drop_column('todos', 'created_at')
    # ### end Alembic commands ###
