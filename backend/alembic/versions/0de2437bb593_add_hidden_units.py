"""Add hidden units

Revision ID: 0de2437bb593
Revises: 6e9f7dfcb356
Create Date: 2023-08-20 22:15:38.635192

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0de2437bb593"
down_revision = "6e9f7dfcb356"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("units", sa.Column("hidden", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("units", "hidden")
    # ### end Alembic commands ###
