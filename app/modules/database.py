from fastapi import HTTPException


class database:
    def __init__(self):
        self.users = {}
    def check_register(self, email):
        if email in self.users:
            raise HTTPException(status_code=400, detail="User already exists.")
        return email
    def check_login(self, email):
        if email not in self.users:       
            raise HTTPException(status_code=404, detail="User not found.")
        return email
    
    def get_users(self):
        return self.users
    
    def set_users(self, users):
        self.users = users

# ✅ Global shared instance
db_instance = database()