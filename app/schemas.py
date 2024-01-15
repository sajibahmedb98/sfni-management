from pydantic import BaseModel
from enum import Enum


class EmployeeRole(str, Enum):
    operator = 'operator'
    staff = 'staff'
    manager = 'manager'


class EmployeeBase(BaseModel):
    name: str
    phone_number: str
    role: EmployeeRole
    base_salary: int

    class Config:
        # from_attributes = True
        from_attributes = True


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int
    
class EmployeeUpdate(BaseModel):
    pass
