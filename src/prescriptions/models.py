from sqlalchemy import (
    Column, Integer, DateTime, ForeignKey, Text
)
from sqlalchemy.orm import relationship
from datetime import datetime

from src.database import Base

class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    diagnosis_id = Column(Integer, ForeignKey("diagnoses.id", ondelete="CASCADE"))
    medication = Column(Text, nullable=False)
    dosage = Column(Text, nullable=False)
    duration = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    diagnosis = relationship("Diagnosis", back_populates="prescriptions")
