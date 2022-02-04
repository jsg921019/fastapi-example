"""add user table

Revision ID: 96715055c3bc
Revises: ab7f7ca9a805
Create Date: 2022-02-05 04:46:23.128920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "96715055c3bc"
down_revision = "ab7f7ca9a805"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
