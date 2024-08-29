from pydantic import BaseModel

class Animal(BaseModel):
    name: str
    habitad: str
    age: int
    type: str
