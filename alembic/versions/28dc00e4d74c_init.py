"""Init

Revision ID: 28dc00e4d74c
Revises: 2f6d69cb6578
Create Date: 2025-03-09 22:45:37.372851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28dc00e4d74c'
down_revision: Union[str, None] = '2f6d69cb6578'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('specialty', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_doctors_id'), 'doctors', ['id'], unique=False)
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('class_name', sa.String(length=10), nullable=True),
    sa.Column('parent_contact', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_students_id'), 'students', ['id'], unique=False)
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('appointment_date', sa.DateTime(), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_appointments_id'), 'appointments', ['id'], unique=False)
    op.create_table('diagnoses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('diagnosis', sa.Text(), nullable=False),
    sa.Column('diagnosis_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_diagnoses_id'), 'diagnoses', ['id'], unique=False)
    op.create_table('medical_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('blood_type', sa.String(length=3), nullable=False),
    sa.Column('allergies', sa.Text(), nullable=True),
    sa.Column('chronic_diseases', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_medical_records_id'), 'medical_records', ['id'], unique=False)
    op.create_table('vaccinations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('vaccine_name', sa.String(length=100), nullable=False),
    sa.Column('vaccination_date', sa.Date(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vaccinations_id'), 'vaccinations', ['id'], unique=False)
    op.create_table('prescriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diagnosis_id', sa.Integer(), nullable=True),
    sa.Column('medication', sa.Text(), nullable=False),
    sa.Column('dosage', sa.Text(), nullable=False),
    sa.Column('duration', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['diagnosis_id'], ['diagnoses.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_prescriptions_id'), 'prescriptions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_prescriptions_id'), table_name='prescriptions')
    op.drop_table('prescriptions')
    op.drop_index(op.f('ix_vaccinations_id'), table_name='vaccinations')
    op.drop_table('vaccinations')
    op.drop_index(op.f('ix_medical_records_id'), table_name='medical_records')
    op.drop_table('medical_records')
    op.drop_index(op.f('ix_diagnoses_id'), table_name='diagnoses')
    op.drop_table('diagnoses')
    op.drop_index(op.f('ix_appointments_id'), table_name='appointments')
    op.drop_table('appointments')
    op.drop_index(op.f('ix_students_id'), table_name='students')
    op.drop_table('students')
    op.drop_index(op.f('ix_doctors_id'), table_name='doctors')
    op.drop_table('doctors')
    # ### end Alembic commands ###
