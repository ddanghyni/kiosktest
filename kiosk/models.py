from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


#! 옵션 테이블
class Option(Base):
    __tablename__ = 'option'
    __table_args__ = {'schema': 'kiosk'}
    option_pk = Column(Integer, primary_key=True, autoincrement=True)
    option_name = Column(String(50), nullable=False)
    option_price = Column(Integer, nullable=False)
#todo 이거 옵션 테이블에 카테고리 pk나 menu pk를 넣어을까??

#! 카테고리 목록 테이블
class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'kiosk'}
    category_pk = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(50), nullable=False)
    

#! 메뉴 테이블

class Menu(Base):
    __tablename__ = 'menu'
    __table_args__ = {'schema': 'kiosk'}
    menu_pk = Column(Integer, primary_key=True, autoincrement=True)
    menu_name = Column(String(50), nullable=False)
    menu_price = Column(Integer, nullable=False)
    menu_description = Column(String(50), nullable=False)
    category_pk = Column(Integer, ForeignKey('kiosk.categories.category_pk'))
    category = relationship('Categories', backref='menu')

#! 주문자 정보 테이블
class Orderer(Base):
    __tablename__ = 'orderer'
    __table_args__ = {'schema': 'kiosk'}
    orderer_id = Column(Integer, primary_key=True, index = True)
    orderer_name = Column(String(50), nullable=False)
    orderer_phone = Column(String(50), nullable=False)
    
#! 주문 상세 테이블

# class OrderDetail(Base):
#     __tablename__ = 'order_detail'
#     __table_args__ = {'schema': 'kiosk'}
#     order_detail_pk = Column(Integer, primary_key=True, autoincrement=True)
#     orderer_id = Column(Integer, ForeignKey('kiosk.orderer.orderer_id'))
#     order = relationship('Orderer', backref='order_detail')
#     menu_pk = Column(Integer, ForeignKey('kiosk.menu.menu_pk'))
#     menu = relationship('Menu', backref='order_detail', lazy="joined") # lazy="joined" 추가
#     options_pk = Column(Integer, ForeignKey('kiosk.option.option_pk'))
#     option = relationship('Option', backref='order_detail', lazy="joined")#! 추가함.
order_option_table = Table(
    "order_option",
    Base.metadata,
    Column("order_detail_pk", Integer, ForeignKey("kiosk.order_detail.order_detail_pk")),
    Column("option_pk", Integer, ForeignKey("kiosk.option.option_pk"))
)

class OrderDetail(Base):
    __tablename__ = 'order_detail'
    __table_args__ = {'schema': 'kiosk'}
    order_detail_pk = Column(Integer, primary_key=True, autoincrement=True)
    orderer_id = Column(Integer, ForeignKey('kiosk.orderer.orderer_id'))
    order = relationship('Orderer', backref='order_detail')
    menu_pk = Column(Integer, ForeignKey('kiosk.menu.menu_pk'))
    menu = relationship('Menu', backref='order_detail', lazy="joined")
    options = relationship("Option", secondary=order_option_table, backref='order_details')  # Change to many-to-many relationship


#



    
