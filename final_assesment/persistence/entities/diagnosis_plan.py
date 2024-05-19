from sqlalchemy import Column, Integer, Date, String, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DiagnosisPlan(Base):
    __tablename__ = "Diagnosis_Plan"
    diagnosis_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, nullable=False)
    diagnosis_details = Column(String)
    diagnosis_date = Column(Date)

    ForeignKeyConstraint(
        ['patient_id'], ['Patient.patient_id']
    )
