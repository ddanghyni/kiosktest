"""empty message

Revision ID: ef171a7c478c
Revises: d62a0b31850a
Create Date: 2023-08-01 15:21:50.322724

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ef171a7c478c'
down_revision = 'd62a0b31850a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_option')
    op.drop_table('options')
    op.drop_constraint('menu_ibfk_1', 'menu', type_='foreignkey')
    op.create_foreign_key(None, 'menu', 'categories', ['category_pk'], ['category_pk'], source_schema='kiosk', referent_schema='kiosk')
    op.drop_constraint('order_detail_ibfk_2', 'order_detail', type_='foreignkey')
    op.drop_constraint('order_detail_ibfk_1', 'order_detail', type_='foreignkey')
    op.create_foreign_key(None, 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'], source_schema='kiosk', referent_schema='kiosk')
    op.create_foreign_key(None, 'order_detail', 'menu', ['menu_pk'], ['menu_pk'], source_schema='kiosk', referent_schema='kiosk')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('order_detail_ibfk_1', 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'])
    op.create_foreign_key('order_detail_ibfk_2', 'order_detail', 'menu', ['menu_pk'], ['menu_pk'])
    op.drop_constraint(None, 'menu', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('menu_ibfk_1', 'menu', 'categories', ['category_pk'], ['category_pk'])
    op.create_table('options',
    sa.Column('option_pk', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('option_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('option_price', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('option_pk'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('order_option',
    sa.Column('order_option_pk', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_detail_pk', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('option_pk', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['option_pk'], ['options.option_pk'], name='order_option_ibfk_1'),
    sa.ForeignKeyConstraint(['order_detail_pk'], ['order_detail.order_detail_pk'], name='order_option_ibfk_2'),
    sa.PrimaryKeyConstraint('order_option_pk'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
