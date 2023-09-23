from fastapi import Depends, FastAPI
from fastapi_pagination import add_pagination

from services.user import get_current_active_user

from routers import user, auth, meal

app = FastAPI()

app.include_router(auth.router, prefix='/api/v1')
app.include_router(user.router, prefix='/api/v1',
                   dependencies=[Depends(get_current_active_user)],)
app.include_router(meal.router, prefix='/api/v1',
                   dependencies=[Depends(get_current_active_user)])

add_pagination(app)


@app.get("/")
async def root():
    return {"message": "Heath Applications API"}
