import enum
from pydantic import BaseModel
from classes.Menu import Menu


class DRINK_CATEGORY(enum.Enum):
    coffee = 1
    tea = 2
    others = 3


class DRINK_TYPE(enum.Enum):
    hot = 1
    cold = 2


class DRINK_SIZE(enum.Enum):
    small = 1
    medium = 2
    large = 3


class Drink(Menu):
    category: DRINK_CATEGORY
    type: DRINK_TYPE
    size: DRINK_SIZE


class DrinkCreate(BaseModel):
    name: str
    description: str
    price: int
    category: DRINK_CATEGORY
    type: DRINK_TYPE
    size: DRINK_SIZE
