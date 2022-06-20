import uvicorn

from fastapi import FastAPI
from routes import bike_routes

app = FastAPI()
app.include_router(bike_routes)

if __name__ == '__main__':

    uvicorn.run(app="main:app", reload=True, host='127.0.0.1', port=8001)


