from sqlalchemy.orm import Session
from models.user import User as UserModel
from schemas.user import User as UserSchema
from passlib.context import CryptContext

crypto_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_all_users(db: Session): 
    return db.query(UserModel).all()

def get_users_by_id(db: Session, id: int): 
    return db.query(UserModel).filter(UserModel.id == id).first()

def create_user(db: Session, user: UserSchema):
    
	db_user = UserModel( username = user.username,
						email = user.email,
      					password = crypto_context.hash(user.password) )
    
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user
