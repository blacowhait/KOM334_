from sqlalchemy import create_engine, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base


DB_TYPE = "postgresql"
DB_PORT = "5432"
DB_HOST = "localhost"
DB_USERNAME = "postgres"
DB_PASSWORD = "root"
DB_NAME = "KOM334"


# connstring = "postgresql://postgres:root@localhost:5432/KOM334"
connstring = "sqlite:///./KOM334.db?check_same_thread=False"
engine = create_engine(connstring, echo=False)

sqlalchemy_session = sessionmaker(bind=engine)


def get_db() -> Session:
    db = sqlalchemy_session()
    return db


Base = declarative_base()


class Food_DB(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    category = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(
        timezone=True), default=func.now(), onupdate=func.current_timestamp())


class Drink_DB(Base):
    __tablename__ = 'drink'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    category = Column(String)
    type = Column(String)
    size = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(
        timezone=True), default=func.now(), onupdate=func.current_timestamp())


class Order_DB(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    total_price = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(
        timezone=True), default=func.now(), onupdate=func.current_timestamp())
    buyer_id = Column(Integer, ForeignKey("buyer.id"))


class Buyer_DB(Base):
    __tablename__ = 'buyer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    whatsapp = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(
        timezone=True), default=func.now(), onupdate=func.current_timestamp())
    orders = relationship("Order_DB")


class Order_Food(Base):
    __tablename__ = "order_food"
    order_id = Column(Integer, ForeignKey("order.id"), primary_key=True)
    food_id = Column(Integer, ForeignKey("food.id"), primary_key=True)


class Order_Drink(Base):
    __tablename__ = "order_drink"
    order_id = Column(Integer, ForeignKey("order.id"), primary_key=True)
    drink_id = Column(Integer, ForeignKey("drink.id"), primary_key=True)


Base.metadata.create_all(bind=engine)
