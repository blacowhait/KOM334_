from datetime import datetime
from enum import Enum, auto
from pydantic import BaseModel


class HistoryType(Enum):
    history_a = auto()
    history_b = auto()
    history_c = auto()


class Actions(Enum):
    first_option = auto()
    second_option = auto()
    third_option = auto()


class HistorySchemaBase(BaseModel):
    tool_id: str
    history_type: HistoryType
    desc: str
    next_action: Actions
    date: datetime


class HistoryCreate(HistorySchemaBase):
    pass


class HistoryUpdate(HistorySchemaBase):
    pass
