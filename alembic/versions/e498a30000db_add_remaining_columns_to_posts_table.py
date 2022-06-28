"""add remaining columns to posts table

Revision ID: e498a30000db
Revises: 831ab4f434b4
Create Date: 2022-06-27 15:10:44.586248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e498a30000db'
down_revision = '831ab4f434b4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean,
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')))

    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', "created_at")
    pass
