"""empty message

Revision ID: 2838c8b93aa4
Revises: d905197a03c3
Create Date: 2023-08-01 23:26:23.401978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2838c8b93aa4'
down_revision = 'd905197a03c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('menu_ibfk_1', 'menu', type_='foreignkey')
    op.create_foreign_key(None, 'menu', 'categories', ['category_pk'], ['category_pk'], source_schema='kiosk', referent_schema='kiosk')
    op.drop_constraint('order_detail_ibfk_1', 'order_detail', type_='foreignkey')
    op.drop_constraint('order_detail_ibfk_2', 'order_detail', type_='foreignkey')
    op.create_foreign_key(None, 'order_detail', 'menu', ['menu_pk'], ['menu_pk'], source_schema='kiosk', referent_schema='kiosk')
    op.create_foreign_key(None, 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'], source_schema='kiosk', referent_schema='kiosk')
    op.drop_constraint('order_option_ibfk_2', 'order_option', type_='foreignkey')
    op.drop_constraint('order_option_ibfk_1', 'order_option', type_='foreignkey')
    op.create_foreign_key(None, 'order_option', 'order_detail', ['order_detail_pk'], ['order_detail_pk'], referent_schema='kiosk')
    op.create_foreign_key(None, 'order_option', 'option', ['option_pk'], ['option_pk'], referent_schema='kiosk')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order_option', type_='foreignkey')
    op.drop_constraint(None, 'order_option', type_='foreignkey')
    op.create_foreign_key('order_option_ibfk_1', 'order_option', 'option', ['option_pk'], ['option_pk'])
    op.create_foreign_key('order_option_ibfk_2', 'order_option', 'order_detail', ['order_detail_pk'], ['order_detail_pk'])
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('order_detail_ibfk_2', 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'])
    op.create_foreign_key('order_detail_ibfk_1', 'order_detail', 'menu', ['menu_pk'], ['menu_pk'])
    op.drop_constraint(None, 'menu', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('menu_ibfk_1', 'menu', 'categories', ['category_pk'], ['category_pk'])
    # ### end Alembic commands ###
