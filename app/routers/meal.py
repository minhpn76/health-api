from fastapi import APIRouter
from typing import Union
from fastapi_pagination import Page, paginate

from db.meal import *
from models.meal import Meal

router = APIRouter(
    prefix="/meal",
    tags=["meal"],
    responses={404: {"description": "Not found"}},
)


@router.get("/types")
async def get_meal_types():
    return fake_meal_type_db


@router.get("/", response_model=Page[Meal])
async def get_meals(meal_type: Union[str, None] = None):
    if not meal_type:
        return paginate(fake_meals_db)

    meal_data = []
    for meal in fake_meals_db:
        if meal["type"] == meal_type:
            meal_data.append(meal)

    return paginate(meal_data)
