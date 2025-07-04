"""change user table field

Revision ID: 2eaf7bc1ec24
Revises: 672afe1788aa
Create Date: 2025-05-31 23:05:44.520478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2eaf7bc1ec24'
down_revision: Union[str, None] = '672afe1788aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('password', sa.String(length=128), nullable=False))
    op.drop_column('Users', 'password_hash')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_column('Users', 'password')
    # ### end Alembic commands ###
