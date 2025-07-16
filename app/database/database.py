from sqlmodel import SQLModel, create_engine

from app.models.user import User
from app.models.medical_speciality import MedicalSpeciality
from app.models.doctor import Doctor
from app.models.state import State
from app.models.doctor_crm import DoctorCrm
from app.models.doctor_medical_speciality import DoctorMedicalSpeciality
from app.models.medical_record import MedicalRecord

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)
