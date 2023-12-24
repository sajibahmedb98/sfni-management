from fastapi import APIRouter, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/employee",
    tags=["Employee"],
)


list = []


@router.post("/")
async def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = models.Employee(**employee.model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    # list.append(employee)

    return new_employee


@router.get("/")
def get_employees():
    return {"message": "Employee retrrrrieved"}
