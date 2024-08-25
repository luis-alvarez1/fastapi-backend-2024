from fastapi import APIRouter, status, HTTPException
from schemas.animal import Animal

router = APIRouter(prefix="/animals")

animals_list = [
	Animal(id=1, name="tigre", habitad="selva", age=4, type="felino grande"),
	Animal(id=2, name="leon", habitad="selva", age=2, type="felino grande"),
	Animal(id=3, name="pantera", habitad="sabana", age=1, type="felino grande"),
	Animal(id=4, name="jaguar", habitad="selva", age=6, type="felino grande")
]


@router.get("/")
async def get_all_animals():
	return animals_list

@router.get("/{id}", response_model=Animal, status_code=status.HTTP_200_OK)
async def get_animal_by_id(id: str):
    
    found = False
    for animal in animals_list:
        if animal.id == int(id):
            found = True
            return animal
    
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
    
@router.post("/")
async def create_animal(animal: Animal):
    pass
