from datetime import datetime
from pydantic import BaseModel

from database import HistoryModel
from schema import Actions, HistorySchemaBase, HistoryType


class BaseHistory(BaseModel):
    id: int
    tool_id: str
    desc: str
    next_action: Actions
    date: datetime

    class Config:
        orm_mode = True


class HistoryA(BaseHistory):
    history_type = HistoryType.history_a

    def __init___(self, obj: HistorySchemaBase | HistoryModel):
        print(obj)
        # if hasattr(obj, "id"):
        #     self.id = obj.id
        # self.tool_id = obj.tool_id
        # self.desc = obj.desc
        # self.next_action = obj.next_action
        # self.date = obj.date

    def create():
        pass

    def read():
        pass

    def readByToolId():
        pass

    def update():
        pass

    def delete():
        pass
