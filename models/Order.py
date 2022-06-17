import datetime
from pydantic import BaseModel
from models.Buyer import Buyer
from models.Menu import Menu


class Order():
    status: str
    total_price: str
    datetime: datetime.datetime
    menu: Menu
    buyer: Buyer
