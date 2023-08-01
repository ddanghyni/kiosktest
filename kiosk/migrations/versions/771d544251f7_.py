"""empty message

Revision ID: 771d544251f7
Revises: 614b5249497d
Create Date: 2023-08-01 14:55:49.128407

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '771d544251f7'
down_revision = '614b5249497d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_constraint('menu_ibfk_1', 'menu', type_='foreignkey')
    op.create_foreign_key(None, 'menu', 'categories', ['category_pk'], ['category_pk'], source_schema='kiosk', referent_schema='kiosk')
    op.drop_constraint('order_detail_ibfk_1', 'order_detail', type_='foreignkey')
    op.drop_constraint('order_detail_ibfk_2', 'order_detail', type_='foreignkey')
    op.create_foreign_key(None, 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'], source_schema='kiosk', referent_schema='kiosk')
    op.create_foreign_key(None, 'order_detail', 'menu', ['menu_pk'], ['menu_pk'], source_schema='kiosk', referent_schema='kiosk')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('order_detail_ibfk_2', 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'])
    op.create_foreign_key('order_detail_ibfk_1', 'order_detail', 'menu', ['menu_pk'], ['menu_pk'])
    op.drop_constraint(None, 'menu', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('menu_ibfk_1', 'menu', 'categories', ['category_pk'], ['category_pk'])
    op.create_table('items',
    sa.Column('item_pk', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('item_pk'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
