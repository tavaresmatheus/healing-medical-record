from sqlmodel import Session, create_engine

from app.config.config import Settings
from app.models.user import User
from app.models.medical_speciality import MedicalSpeciality
from app.models.doctor import Doctor
from app.models.state import State
from app.models.doctor_crm import DoctorCrm
from app.models.doctor_medical_speciality import DoctorMedicalSpeciality
from app.models.medical_record import MedicalRecord

settings = Settings()
connection_url = f'postgresql://{settings.database_user}:{settings.database_password}@healing-medical-record-postgres:5432/{settings.app_database}'

engine = create_engine(
    connection_url,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800
)

def get_session():
    with Session as session:
        yield session
