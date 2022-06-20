from fastapi import APIRouter

bike_routes = APIRouter()

@bike_routes.get('/bikes')
def get_bikes():
    return []