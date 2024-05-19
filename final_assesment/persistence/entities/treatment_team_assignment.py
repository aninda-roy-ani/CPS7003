from sqlalchemy import Column, Integer, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TreatmentTeamAssignment(Base):
    __tablename__ = "Treatment_Team_Assignment"
    assignment_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer)
    user_id = Column(Integer)

    ForeignKeyConstraint(
        ['patient_id', 'user_id'], ['Patient.patient_id', 'User.user_id']
    )
