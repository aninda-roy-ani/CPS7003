from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

Base = declarative_base()

class ModuleTutor(Base):
    __tablename__ = "Module_Tutor"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(String, nullable=False)
    ModuleID = Column(Integer, nullable=False)

    ForeignKeyConstraint(
        ["UserID", "ModuleID"], ["User.ID", "Module.ID"]
    )