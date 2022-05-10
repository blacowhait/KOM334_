from click import echo
from sqlalchemy import Column, DateTime, Enum, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from schema import Actions, HistoryType


CONNECTION_STRING = "postgresql://postgres:root@localhost/KOM334"

engine = create_engine(CONNECTION_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class HistoryModel(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    tool_id = Column(String)
    history_type = Column(Enum(HistoryType))
    desc = Column(String)
    next_action = Column(Enum(Actions))
    date = Column(DateTime)
