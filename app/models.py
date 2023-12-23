from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    create_at = Column(DateTime())
