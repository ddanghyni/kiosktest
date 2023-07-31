from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

#! 카테고리 목록 테이블
class Categories(Base):
    __tablename__ = 'categories'
    category_pk = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, nullable=False)
    

#! 메뉴 테이블

class Menu(Base):
    __tablename__ = 'menu'
    menu_pk = Column(Integer, primary_key=True, autoincrement=True)
    menu_name = Column(String, nullable=False)
    menu_price = Column(Integer, nullable=False)
    menu_description = Column(String, nullable=False)
    category_pk = Column(Integer, ForeignKey('categories.category_pk'))
    category = relationship('Categories', backref='menu')

#! 주문자 정보 테이블
class Orderer(Base):
    __tablename__ = 'orderer'
    orderer_id = Column(Integer, primary_key=True, autoincrement=True)
    orderer_name = Column(String, nullable=False)
    orderer_phone = Column(String, nullable=False)
    
    



#! 주문 상세 테이블

class OrderDetail(Base):
    __tablename__ = 'order_detail'
    order_detail_pk = Column(Integer, primary_key=True, autoincrement=True)
    orderer_id = Column(Integer, ForeignKey('orderer.orderer_id'))
    order = relationship('Orderer', backref='order_detail')
    menu_pk = Column(Integer, ForeignKey('menu.menu_pk'))
    menu = relationship('Menu', backref='order_detail')
    menu_count = Column(Integer, nullable=False)


#!! 옵션 추가 테이블 !!

class Option(Base):
    __tablename__ = 'options'
    option_pk = Column(Integer, primary_key=True, autoincrement=True)
    option_name = Column(String, nullable=False)
    option_price = Column(Integer, nullable=False)

class OrderOption(Base):
    __tablename__ = 'order_option'
    order_option_pk = Column(Integer, primary_key=True, autoincrement=True)
    order_detail_pk = Column(Integer, ForeignKey('order_detail.order_detail_pk'), nullable=False)
    option_pk = Column(Integer, ForeignKey('options.option_pk'), nullable=False)
    option = relationship('Option', backref='order_option')
    order_detail = relationship('OrderDetail', backref='order_option')


    



    
