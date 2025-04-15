from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()

class DataUpdate(BaseModel):
    updated_title: str
    updated_content: str
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

        #Format     "Title" : "Content"    
        self.notes = []

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_notes(self):
        return [note.dict() for note in self.notes] #self.notes
    
    def add_notes(self, title, content):
        note = Notes(title=title, content=content)          #{title : content}
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
        update_data = "updated data bip bop zip"
        for index, note in enumerate(self.notes):
            if note.title == title:
                self.notes[index] = "updated data bip bop zip"
                return self.notes
        raise HTTPException(status_code=404, detail="Note not found")
#    def test_notes(self):
#        print(f'{self.notes}')
#        for i in self.notes:
#            print(f"i: {i} \ntitle:{i.title}")
user = User("Café", "rammoscafe@gmail.com", "abc123")
user.add_notes("cli-test", "text prompt lorem bla bla bla")
#user.test_notes()
#user.add_notes("Day 1", "This is my first note")
#notes = user.get_notes()
#user.add_notes("Day 2", "This is my second note")
#print(f"{user.get_notes()[0].title} : {user.get_notes()[0].content}")



@app.post("/notes")
def add_note(note: CreateNote):
    user.add_notes(note.title, note.content)
    return {"message": "Note added successfully"}


@app.get("/note")
async def get_note():
    return user.get_notes()

@app.get("/note/{title}")
async def get_note_on_title(title: str):
    return user.get_note_on_title(title)


@app.delete("/notes/{title}")
async def delete_note_on_title(title: str):
    return user.delete_note_on_title(title)

@app.put("/notes/{title}")
async def update_note(title: str, update_data: DataUpdate):
    return user.update_note(title, update_data)