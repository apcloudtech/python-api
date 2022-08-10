"""add user table

Revision ID: 76647ca80c38
Revises: bb67a4019903
Create Date: 2022-06-27 12:24:33.367035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76647ca80c38'
down_revision = 'bb67a4019903'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
