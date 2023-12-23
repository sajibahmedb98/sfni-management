from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    phone_number: str

    class Config:
        from_attributes = True
