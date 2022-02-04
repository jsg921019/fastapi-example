"""add foreign-key to posts table

Revision ID: b69d8db2f844
Revises: 96715055c3bc
Create Date: 2022-02-05 04:59:32.554473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b69d8db2f844"
down_revision = "96715055c3bc"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
