from fastapi import FastAPI
from modules.database import db_instance
from modules.user import User
from routes.user_routes import router as user_router
from routes.notes_routes import router as notes_router

app = FastAPI()
app.include_router(user_router)
app.include_router(notes_router)
database = db_instance
