from pydantic import BaseModel, EmailStr

class LoginUserCredentialsInputModel(BaseModel):
    email: str
    password: str
    client_id: str
    client_secret: str