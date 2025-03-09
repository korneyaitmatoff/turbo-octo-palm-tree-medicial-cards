from sqlalchemy import (
    Column, Integer, DateTime, ForeignKey, Text
)
from sqlalchemy.orm import relationship
from datetime import datetime

from src.database import Base


class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    doctor_id = Column(Integer, ForeignKey("doctors.id", ondelete="SET NULL"), nullable=True)
    diagnosis = Column(Text, nullable=False)
    diagnosis_date = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="diagnoses")
    doctor = relationship("Doctor", back_populates="diagnoses")
    prescriptions = relationship("Prescription", back_populates="diagnosis")
