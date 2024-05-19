from sqlalchemy import Column, Integer, Date, String, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TreatmentPlan(Base):
    __tablename__ = "Treatment_Plan"
    treatment_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, nullable=False)
    diagnosis_id = Column(Integer, nullable=False)
    treatment_details = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    ForeignKeyConstraint(
        ['patient_id', 'diagnosis_id'], ['Patient.patient_id', 'Diagnosis.diagnosis_id']
    )
