"""create posts table

Revision ID: 75b9dd1ddeb0
Revises: 
Create Date: 2022-02-05 04:15:38.829443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "75b9dd1ddeb0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table("posts")
