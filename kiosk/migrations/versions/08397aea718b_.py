"""empty message

Revision ID: 08397aea718b
Revises: 496cac301c6b
Create Date: 2023-08-10 21:20:20.353420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08397aea718b'
down_revision = '496cac301c6b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('face_analysis',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('emotion', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('menu_ibfk_1', 'menu', type_='foreignkey')
    op.create_foreign_key(None, 'menu', 'categories', ['category_pk'], ['category_pk'], source_schema='kiosk', referent_schema='kiosk')
    op.drop_constraint('order_detail_ibfk_2', 'order_detail', type_='foreignkey')
    op.drop_constraint('order_detail_ibfk_1', 'order_detail', type_='foreignkey')
    op.create_foreign_key(None, 'order_detail', 'menu', ['menu_pk'], ['menu_pk'], source_schema='kiosk', referent_schema='kiosk')
    op.create_foreign_key(None, 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'], source_schema='kiosk', referent_schema='kiosk')
    op.drop_constraint('order_option_ibfk_2', 'order_option', type_='foreignkey')
    op.drop_constraint('order_option_ibfk_1', 'order_option', type_='foreignkey')
    op.create_foreign_key(None, 'order_option', 'order_detail', ['order_detail_pk'], ['order_detail_pk'], referent_schema='kiosk')
    op.create_foreign_key(None, 'order_option', 'option_', ['option_pk'], ['option_pk'], referent_schema='kiosk')
    op.drop_constraint('recommended_menu_ibfk_1', 'recommended_menu', type_='foreignkey')
    op.create_foreign_key(None, 'recommended_menu', 'menu', ['menu_pk'], ['menu_pk'], source_schema='kiosk', referent_schema='kiosk')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recommended_menu', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('recommended_menu_ibfk_1', 'recommended_menu', 'menu', ['menu_pk'], ['menu_pk'])
    op.drop_constraint(None, 'order_option', type_='foreignkey')
    op.drop_constraint(None, 'order_option', type_='foreignkey')
    op.create_foreign_key('order_option_ibfk_1', 'order_option', 'order_detail', ['order_detail_pk'], ['order_detail_pk'])
    op.create_foreign_key('order_option_ibfk_2', 'order_option', 'option_', ['option_pk'], ['option_pk'])
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.drop_constraint(None, 'order_detail', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('order_detail_ibfk_1', 'order_detail', 'orderer', ['orderer_id'], ['orderer_id'])
    op.create_foreign_key('order_detail_ibfk_2', 'order_detail', 'menu', ['menu_pk'], ['menu_pk'])
    op.drop_constraint(None, 'menu', schema='kiosk', type_='foreignkey')
    op.create_foreign_key('menu_ibfk_1', 'menu', 'categories', ['category_pk'], ['category_pk'])
    op.drop_table('face_analysis')
    # ### end Alembic commands ###