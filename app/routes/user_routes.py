from fastapi import APIRouter
from modules.user import User
from modules.models import registerUser
from modules.database import db_instance as database

router = APIRouter()
@router.post("/")
def registration(register: registerUser):
    database.check_register(register.email)
    database.users[register.email] = User(register.name, register.email, register.password)
    return {"message": "{register.name} registred"}

