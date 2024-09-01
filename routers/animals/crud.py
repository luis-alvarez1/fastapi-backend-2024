from sqlalchemy.orm import Session

from models.animal import Animal as AnimalModel
from schemas.animal import Animal as AnimalSchema

# En este archivo van las funciones que interactúan con la DB

def get_animals(db: Session):
    # devuelve los animales de DB
    return db.query(AnimalModel).all()


def get_animal_by_id(db: Session, id: int):
    # devuelve animal por id
    return db.query(AnimalModel).filter(AnimalModel.id == id).first()



def create_animal(db: Session, animal: AnimalSchema):
    # VALIDACIONES...
    
    # crea un animal con el modelo. SQLAlchemy se encarga de ponerle ID
    db_animal = AnimalModel( name=  animal.name , habitad=animal.habitad, age= animal.age, type= animal.type )
    
    # lo agrega a la base de datos (sin impactar DB)
    db.add(db_animal)
    
    
    # impacta DB
    db.commit()
    
    # obtiene el objeto creado desde DB
    db.refresh(db_animal)
    
    return db_animal



def update_animal(db: Session, id: str, animal: AnimalSchema)-> AnimalModel | None:
    # mira si existe
	animal_to_update = get_animal_by_id(db=db, id=id)

	# si exite, hace los cambios en db
	if animal_to_update:
		# actualiza los datos de db con los que me llegan
		db.query(AnimalModel).filter(AnimalModel.id == id).update({
			AnimalModel.name : animal.name,
			AnimalModel.age : animal.age,
			AnimalModel.type : animal.type,
			AnimalModel.habitad : animal.habitad,
		})
		db.commit()
		# retorno el animal actualizado de db
		animal = get_animal_by_id(db=db, id=id)
		
  
		return animal


 
def delete_animal(db: Session, id: str) -> AnimalModel | None:
	# mira si existe
	animal_to_delete = get_animal_by_id(db=db, id=id)
	# borra el animal
	db.query(AnimalModel).filter(AnimalModel.id == id).delete()
	db.commit()
 
	
	return animal_to_delete