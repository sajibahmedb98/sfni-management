from typing import Dict, Any

from fastapi import APIRouter, Response, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/employee",
    tags=["Employee"],
)


# list = []

# create employee
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = models.Employee(**employee.model_dump())
    existing_employee = db.query(models.Employee).filter(
        models.Employee.phone_number == employee.phone_number).first()
    if existing_employee:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Phone Number already exist')

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    # list.append(employee)

    return new_employee

# get all employees


@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(models.Employee).all()

    return employees

# get employee by id


@router.get("/{id}", response_model=schemas.EmployeeOut)
def get_employee(id: int, db: Session = Depends(get_db)):
    employee_id = db.query(models.Employee).filter(
        models.Employee.id == id).first()
    if not employee_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Employee does not exist')

    employee = db.query(models.Employee).filter(
        models.Employee.id == id).first()

    return employee


# delete employee by id
@router.delete("/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(
        models.Employee.id == id).first()

    employee_name = db.query(models.Employee.name).first()

    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{employee_name} does not exist")
    db.delete(employee)
    db.commit()

    return {"message": f"Employee {employee_name} has been deleted"}


# update employee by id
@router.put("/{id}")
async def update_employee(id: int, update_data: Dict[str, Any], db: Session = Depends(get_db)):
    existing_employee = db.query(models.Employee).filter(
        models.Employee.id == id).first()
    if not existing_employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Employee does not exist')

    for key, value in update_data.items():
        setattr(existing_employee, key, value)

    db.commit()

    return {"message": "Employee has been updated"}
