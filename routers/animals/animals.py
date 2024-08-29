from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session 
from schemas.animal import Animal as AnimalSchema 
from config.db import SessionLocal
from . import crud

router = APIRouter(prefix="/animals")

animals_list = [
	AnimalSchema( id=1,name="tigre", habitad="selva", age=4, type="felino grande"),
	AnimalSchema( id =2,name="leon", habitad="selva", age=2, type="felino grande"),
	AnimalSchema( id=3,name="pantera", habitad="sabana", age=1, type="felino grande"),
	AnimalSchema( id=4,name="jaguar", habitad="selva", age=6, type="felino grande")
]


# obtiene la información de la conexión db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get_all_animals(db: Session = Depends(get_db)):
	# Devuelve los animales de DB
	animals = crud.get_animals(db=db)
	return animals 

@router.get("/{id}", status_code=status.HTTP_200_OK )
async def get_animal_by_id(id: str, db: Session = Depends(get_db)):
    # obtiene el animal de DB
    animal = crud.get_animal_by_id(db= db, id=id )
    
    # si no hay animal -> 404
    if not animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
    
    # devuelve el animal
    return animal

@router.post("/", response_model=AnimalSchema, status_code=status.HTTP_201_CREATED)
async def create_animal(animal_body: AnimalSchema, db: Session = Depends(get_db)):
    
	return crud.create_animal(db=db, animal=animal_body)

@router.patch("/{id}",  status_code=status.HTTP_200_OK)
async def uptade_animal(id: str, animal_body:AnimalSchema, db: Session = Depends(get_db)):
	animal = crud.update_animal(db=db, id=id, animal=animal_body)

	if not animal:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
  
	return animal


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_animal(id: str, db: Session = Depends(get_db)):
	animal = crud.delete_animal(db=db, id=id)

	if not animal:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
	return animal