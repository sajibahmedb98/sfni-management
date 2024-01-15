
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    phone_number = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)
    base_salary = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
