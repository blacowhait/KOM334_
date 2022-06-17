import enum
from pydantic import BaseModel
from classes.Menu import Menu


class FOOD_CATEGORY(enum.Enum):
    main_course = 1
    dessert = 2
    appetizer = 3
    others = 4


class Food(Menu):
    category: FOOD_CATEGORY


class FoodCreate(BaseModel):
    name: str
    description: str
    price: int
    category: FOOD_CATEGORY
