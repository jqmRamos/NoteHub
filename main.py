from fastapi import FastAPI
from fastapi import Query
from pydantic import BaseModel

app = FastAPI()


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

    def test_notes(self):
        print(f'{self.notes}')
user = User("Café", "rammoscafe@gmail.com", "abc123")
#user.add_notes("Day 1", "This is my first note")
#notes = user.get_notes()
#user.add_notes("Day 2", "This is my second note")
#print(f"{user.get_notes()[0].title} : {user.get_notes()[0].content}")


@app.get("/note")
async def get_note():
    return user.get_notes()

@app.post("/notes")
def add_note(note: CreateNote):
    user.add_notes(note.title, note.content)
    return {"message": "Note added successfully"}



'''
    def get_note_on_title(title):

@app.get("/note/{title}")
async def get_note_on_title():
    return user.get_notes_on_title()

'''