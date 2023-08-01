"""empty message

Revision ID: 69fb0bf5020a
Revises: 771d544251f7
Create Date: 2023-08-01 15:09:02.559567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69fb0bf5020a'
down_revision = '771d544251f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('options',
    sa.Column('option_pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('option_name', sa.String(length=50), nullable=False),
    sa.Column('option_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('option_pk'),
    schema='kiosk'
    )
    op.create_table('order_option',
    sa.Column('order_option_pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_detail_pk', sa.Integer(), nullable=False),
    sa.Column('option_pk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['option_pk'], ['kiosk.options.option_pk'], ),
    sa.ForeignKeyConstraint(['order_detail_pk'], ['kiosk.order_detail.order_detail_pk'], ),
    sa.PrimaryKeyConstraint('order_option_pk'),
    schema='kiosk'
    )
    op.drop_constraint('menu_ibfk_1', 'menu', type_='foreignkey')
    op.create_foreign_key(None, 'menu', 'categories', ['category_pk'], ['category_pk'], source_schema='kiosk', referent_schema='kiosk')
    op.drop_constraint('order_detail_ibfk_1', 'order_detail', type_='foreignkey')
    op.drop_constraint('order_detail_ibfk_2', 'order_detail', type_='foreignkey')
    op.create_foreign_key(None, 'order_detail', 'menu', ['menu_pk'], ['menu_pk'], source_schema='kiosk', referent_schema='kiosk')
    op.create_foreign_key(None, 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'], source_schema='kiosk', referent_schema='kiosk')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('order_detail_ibfk_2', 'order_detail', 'menu', ['menu_pk'], ['menu_pk'])
    op.create_foreign_key('order_detail_ibfk_1', 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'])
    op.drop_constraint(None, 'menu', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('menu_ibfk_1', 'menu', 'categories', ['category_pk'], ['category_pk'])
    op.drop_table('order_option', schema='kiosk')
    op.drop_table('options', schema='kiosk')
    # ### end Alembic commands ###