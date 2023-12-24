from fastapi import FastAPI
from .routes import employee

# Comment out or remove the following line in your main.py
import uvloop
uvloop.install()


app = FastAPI()


app.include_router(employee.router)


@app.get("/")
def home():
    return {"message": "Home"}
