from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

Base = declarative_base()


class Course(Base):
    __tablename__ = "Course"
    CourseID = Column(Integer, primary_key=True, autoincrement=True)
    Award = Column(String, nullable=False)
    Title = Column(String, nullable=False)
    CourseLeader = Column(Integer, nullable=False)
    SubjectID = Column(Integer, nullable=False)

    ForeignKeyConstraint(
        ["CourseLeader", "SubjectID"], ["User.UserID", "Subject.SubjectID"]
    )
