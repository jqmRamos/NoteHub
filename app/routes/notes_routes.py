from fastapi import APIRouter
from modules.models import CreateNote, DataUpdate
from modules.database import db_instance as database

router = APIRouter()
@router.post("/user/{email}/note")
def add_note(email: str, note: CreateNote):
    database.check_login(email)
    user = database.users[email]
    user.add_notes(note.title, note.content)
    return {"message": "Note {note.title} added successfully"}

@router.get("/user/{email}/note")
async def get_note(email: str):
    database.check_login(email)
    user = database.users[email]
    return user.get_notes()

@router.get("/user/{email}/note/{title}")
async def get_note_on_title(email:str, title: str):
    database.check_login(email)
    user = database.users[email]
    return user.get_note_on_title(title)

@router.delete("/user/{email}/notes/{title}")
async def delete_note_on_title(email: str, title: str):
    database.check_login(email)
    user = database.users[email]
    return user.delete_note_on_title(title)

@router.put("/user/{email}/notes/{title}")
async def update_note(email: str, title: str, class_update_data: DataUpdate):
    database.check_login(email)
    user = database.users[email]
    return user.update_note(title, class_update_data)