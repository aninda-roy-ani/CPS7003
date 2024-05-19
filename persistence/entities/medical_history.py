from sqlalchemy import Column, Integer, Date, String, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MedicalHistory(Base):
    __tablename__ = "Medical_History"
    history_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, nullable=False)
    admission_date = Column(Date)
    discharge_date = Column(Date)
    diagnosis = Column(String)
    medical_notes = Column(String)

    ForeignKeyConstraint(
        ['patient_id'], ['Patient.patient_id']
    )
