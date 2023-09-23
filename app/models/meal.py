import datetime
from pydantic import BaseModel


class MealType(BaseModel):
    id: int
    name: str


class Meal(BaseModel):
    id: int
    image: str
    type: str
    datedOn: datetime.datetime
