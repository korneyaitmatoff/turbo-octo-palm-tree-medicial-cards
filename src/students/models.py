from sqlalchemy import (
    Column, Integer, String, Date, DateTime
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    class_name = Column(String(10), nullable=True)
    parent_contact = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    medical_records = relationship("MedicalRecord", back_populates="student")
    appointments = relationship("Appointment", back_populates="student")
    diagnoses = relationship("Diagnosis", back_populates="student")
    vaccinations = relationship("Vaccination", back_populates="student")
