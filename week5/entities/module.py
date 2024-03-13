from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

Base = declarative_base()

class Module(Base):
    __tablename__ = "Module"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Code = Column(String, nullable=False)
    Title = Column(String, nullable=False)
    Level = Column(Integer, nullable=False)
    ModuleLeader = Column(Integer, nullable=False)
    CourseID = Column(Integer, nullable=False)

    ForeignKeyConstraint(
        ["ModuleLeader", "CourseID"],["User.ID", "Course.ID"]
    )