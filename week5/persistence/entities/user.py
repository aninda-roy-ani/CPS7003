from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Email = Column(String, unique=True, nullable=False)
    RoleID = Column(Integer, nullable=False)

    ForeignKeyConstraint(
        ["RoleID"], ["Role.RoleID"]
    )