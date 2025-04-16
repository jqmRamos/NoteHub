from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
users_db = {}

class registerUser(BaseModel):
    name: str
    email: str
    password: str
class DataUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
class CreateNote(BaseModel):
    title: str
    content: str
class Notes(BaseModel):
    title: str
    content: str
class User:
    id = 1
    def __init__(self, name, email, password):
        self.id = User.id
        User.id += 1
        self.name = name
        self.email = email
        self.password = password
        self.notes = [] #Format   object Notes with  "Title" and "Content" atributes

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_notes(self):
        return [note.dict() for note in self.notes] #self.notes
    
    def add_notes(self, title, content):
        note = Notes(title=title, content=content)  #{title : content}
        self.notes.append(note)

    def get_note_on_title(self, title):
        for note in self.notes:
            if note.title == title:
                return note.dict()
        raise HTTPException(status_code=404, detail="Note not found")
    
    def delete_note_on_title(self, title):
        for index, note in enumerate(self.notes):
            if note.title == title:
                self.notes.pop(index)
                return self.notes
        raise HTTPException(status_code=404, detail="Note not found")
    
    def update_note(self, title, update_data=None):
        for index, note in enumerate(self.notes):
            if note.title == title:
                if update_data.title:
                    note.title = update_data.title
                if update_data.content:
                    note.content = update_data.content
                return note.dict()
        raise HTTPException(status_code=404, detail="Note not found")
    
@app.post("/")
def registration(register: registerUser):
    if register.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists.")
    users_db[register.email] = User(register.name, register.email, register.password)
    return {"message": "{register.name} registred"}

@app.post("/user/{email}/note")
def add_note(email: str, note: CreateNote):
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    user = users_db[email]
    user.add_notes(note.title, note.content)
    return {"message": "Note {note.title} added successfully"}

@app.get("/user/{email}/note")
async def get_note(email: str):
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    user = users_db[email]
    return user.get_notes()

@app.get("/user/{email}/note/{title}")
async def get_note_on_title(email:str, title: str):
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    user = users_db[email]
    return user.get_note_on_title(title)

@app.delete("/user/{email}/notes/{title}")
async def delete_note_on_title(email: str, title: str):
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    user = users_db[email]
    return user.delete_note_on_title(title)

@app.put("/user/{email/notes/{title}")
async def update_note(email: str, title: str, class_update_data: DataUpdate):
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    user = users_db[email]
    return user.update_note(title, class_update_data)