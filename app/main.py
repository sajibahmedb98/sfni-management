from fastapi import FastAPI
from .routes import employee


app = FastAPI()


app.include_router(employee.router)


@app.get("/")
def home():
    return {"message": "Home"}
