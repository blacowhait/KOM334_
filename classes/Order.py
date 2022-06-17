import datetime
from pydantic import BaseModel
from classes.Buyer import Buyer
from classes.Menu import Menu


class Order():
    status: str
    total_price: str
    datetime: datetime.datetime
    menu: Menu
    buyer: Buyer
