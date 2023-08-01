"""empty message

Revision ID: 0209c0b7e8a7
Revises: 397451b94ebf
Create Date: 2023-07-28 14:43:14.454939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0209c0b7e8a7'
down_revision = '397451b94ebf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_history')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_history',
    sa.Column('history_id', sa.INTEGER(), nullable=False),
    sa.Column('orderer_id', sa.INTEGER(), nullable=False),
    sa.Column('menu_pk', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['menu_pk'], ['menu.menu_pk'], ),
    sa.ForeignKeyConstraint(['orderer_id'], ['orderer.orderer_id'], ),
    sa.PrimaryKeyConstraint('history_id')
    )
    # ### end Alembic commands ###
