"""add last few columns to posts table

Revision ID: ec8d7d4eed4d
Revises: b69d8db2f844
Create Date: 2022-02-05 05:09:30.137451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ec8d7d4eed4d"
down_revision = "b69d8db2f844"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
