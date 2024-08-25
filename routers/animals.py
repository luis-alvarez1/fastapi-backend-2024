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
    
@router.post("/", response_model=Animal, status_code=status.HTTP_201_CREATED)
async def create_animal(animal_body: Animal):
    
    new_animal = Animal(id= int(animal_body.id),
                        name=animal_body.name,
                        type=animal_body.type,
                        age=animal_body.age,
                        habitad=animal_body.habitad)
    
    animals_list.append(new_animal)
    
    
    for animal_db in animals_list:
        if animal_db.id == new_animal.id:
            return animal_db
        

@router.patch("/{id}", response_model=Animal, status_code=status.HTTP_200_OK)
async def uptade_animal(id: str, animal_body:Animal):
	found = False

	for animal in animals_list:
		if animal.id == int(id):
			found = True
			animals_list.remove(animal)
			animal_to_update =  Animal(id= int(animal_body.id),
						name=animal_body.name,
						type=animal_body.type,
						age=animal_body.age,
						habitad=animal_body.habitad)
			animals_list.append(animal_to_update)
			
	for animal_db in animals_list:
		if animal_db.id == animal_to_update.id:
			return animal_db
	if not found:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")

	
 

