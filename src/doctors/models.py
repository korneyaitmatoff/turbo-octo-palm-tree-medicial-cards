from sqlalchemy import (
    Column, Integer, String, DateTime
)
from sqlalchemy.orm import relationship
from datetime import datetime

from src.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    specialty = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    appointments = relationship("Appointment", back_populates="doctor")
    diagnoses = relationship("Diagnosis", back_populates="doctor")
    vaccinations = relationship("Vaccination", back_populates="doctor")
