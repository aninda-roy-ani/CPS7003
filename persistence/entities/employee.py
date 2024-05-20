from sqlalchemy import Column, Integer, String, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = "Employee"
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    role_id = Column(Integer)

    ForeignKeyConstraint(
        ['role_id'], ['Role.role_id']
    )
