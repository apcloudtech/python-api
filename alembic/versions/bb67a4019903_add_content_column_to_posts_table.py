"""add content column to posts table

Revision ID: bb67a4019903
Revises: 037efdddf92e
Create Date: 2022-06-27 12:20:29.580187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb67a4019903'
down_revision = '037efdddf92e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
