from pydantic import BaseModel
from enum import Enum


class EmployeeRole(str, Enum):
    operator = 'operator'
    staff = 'staff'


class EmployeeCreate(BaseModel):
    name: str
    phone_number: str
    role: EmployeeRole

    class Config:
        from_attributes = True
