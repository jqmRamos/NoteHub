from modules.models import Notes, CreateNote, registerUser, DataUpdate
from fastapi import HTTPException

class User:
    id = 1
    def __init__(self, name, email, password):
        self.id = User.id
        User.id += 1
        self.name = name
        self.email = email
        self.password = password
        self.notes = [] 

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
