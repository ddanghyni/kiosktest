"""empty message

Revision ID: dc040d1dead5
Revises: d658c1c5bd99
Create Date: 2023-07-27 22:27:50.745708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc040d1dead5'
down_revision = 'd658c1c5bd99'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orderer', sa.Column('orderer_address', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orderer', 'orderer_address')
    # ### end Alembic commands ###