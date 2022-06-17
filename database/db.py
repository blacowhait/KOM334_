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
connstring = "sqlite:///./KOM334.db"
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


Base.metadata.create_all(bind=engine)
