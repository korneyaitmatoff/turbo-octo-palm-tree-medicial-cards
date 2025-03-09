from sqlalchemy import create_engine
from sqlalchemy import (
    Column, Integer, String, Date, DateTime, ForeignKey, Text
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

from src.config import (
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST
)

url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
engine = create_engine(url=url)

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


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    blood_type = Column(String(3), nullable=False)
    allergies = Column(Text, nullable=True)
    chronic_diseases = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="medical_records")


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


class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    diagnosis_id = Column(Integer, ForeignKey("diagnoses.id", ondelete="CASCADE"))
    medication = Column(Text, nullable=False)
    dosage = Column(Text, nullable=False)
    duration = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    diagnosis = relationship("Diagnosis", back_populates="prescriptions")


class Vaccination(Base):
    __tablename__ = "vaccinations"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    vaccine_name = Column(String(100), nullable=False)
    vaccination_date = Column(Date, nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="vaccinations")
    doctor = relationship("Doctor", back_populates="vaccinations")
