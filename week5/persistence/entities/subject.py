from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

Base = declarative_base()

class Subject(Base):
    __tablename__ = "Subject"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String, nullable=False)
    SubjectLeader = Column(Integer, nullable=False)

    ForeignKeyConstraint(
        ["SubjectLeader"], ["User.ID"]
    )