from fastapi import APIRouter
from database import get_db

routerExample = APIRouter(prefix='/routesExample')

@router.post('/checkingRoutes')
async def login_for_access():
    return {"message":"all ok"}

