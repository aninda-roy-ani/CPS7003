from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Patient(Base):
    __tablename__ = "Patient"
    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    gender = Column(String)
    contact_no = Column(String)
    address = Column(String)
