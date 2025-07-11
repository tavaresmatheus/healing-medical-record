from sqlmodel import SQLModel, create_engine

from ..models.user import User
from ..models.medical_speciality import MedicalSpeciality
from ..models.doctor import Doctor
from ..models.state import State
from ..models.doctor_crm import DoctorCrm
from ..models.doctor_medical_speciality import DoctorMedicalSpeciality
from ..models.medical_record import MedicalRecord

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
