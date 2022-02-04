"""add content to posts table

Revision ID: ab7f7ca9a805
Revises: 75b9dd1ddeb0
Create Date: 2022-02-05 04:40:49.577610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab7f7ca9a805'
down_revision = '75b9dd1ddeb0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
