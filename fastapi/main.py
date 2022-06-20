from fastapi import FastAPI
from routes import bike_routes

if __name__ == '__main__':
    app = FastAPI()
    app.include_router(bike_routes)

