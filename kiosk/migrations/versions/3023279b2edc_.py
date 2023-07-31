"""empty message

Revision ID: 3023279b2edc
Revises: 8e53f0e19802
Create Date: 2023-07-31 14:46:38.234038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3023279b2edc'
down_revision = '8e53f0e19802'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('options',
    sa.Column('option_pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('option_name', sa.String(), nullable=False),
    sa.Column('option_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('option_pk')
    )
    op.create_table('order_options',
    sa.Column('order_option_pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_detail_pk', sa.Integer(), nullable=False),
    sa.Column('option_pk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['option_pk'], ['options.option_pk'], ),
    sa.ForeignKeyConstraint(['order_detail_pk'], ['order_detail.order_detail_pk'], ),
    sa.PrimaryKeyConstraint('order_option_pk')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_options')
    op.drop_table('options')
    # ### end Alembic commands ###
