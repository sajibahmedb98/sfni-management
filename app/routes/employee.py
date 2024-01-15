from fastapi import APIRouter, Response, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/employee",
    tags=["Employee"],
)


# list = []


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


@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(models.Employee).all()

    return employees


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




@router.delete("/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(
        models.Employee.id == id).first()
    employee_name = db.query(models.Employee.name).first()
    db.delete(employee)
    db.commit()

    return {"message": f"Employee {employee_name} has been deleted"}

@router.put("/{id}")
def update_employee(id: int,employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(
        models.Employee.id == id).first()
    
    
    
    