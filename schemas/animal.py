from pydantic import BaseModel

class Animal(BaseModel):
    id:int
    name: str
    habitad: str
    age: int
    type: str
    
    