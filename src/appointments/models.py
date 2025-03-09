from datetime import datetime

from sqlalchemy import (
    Column, Integer, DateTime, ForeignKey, Text
)
from sqlalchemy.orm import relationship

from src.database import Base



class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    doctor_id = Column(Integer, ForeignKey("doctors.id", ondelete="SET NULL"), nullable=True)
    appointment_date = Column(DateTime, nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")