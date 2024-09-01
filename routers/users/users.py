from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from config.db import SessionLocal
from schemas.user import User as UserSchema
from schemas.token import Token, TokenData
from datetime import timedelta, datetime, timezone
from typing import Annotated
from jwt.exceptions import InvalidTokenError
import jwt
from . import crud

router = APIRouter(prefix="/users")


SECRET_KEY = "backend-2024"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
	db = SessionLocal()
	try:
		yield db
	except:
		db.close()

@router.get("/", status_code=status.HTTP_200_OK)
def get_users(db:Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return users

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_users( user : UserSchema, db:Session = Depends(get_db)):
    db_user = crud.create_user(db= db, user=user)
    return db_user

@router.get("/{id}", status_code=status.HTTP_200_OK )
async def get_user_by_id(id: str, db: Session = Depends(get_db)):
    user = crud.get_users_by_id(db= db, id=id )
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user

# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not password == user.password:
#         return False
#     return user




# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = datetime.now(timezone.utc) + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def authorizate(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_403_FORBIDDEN,
#         detail="Could not validate credentials",
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("user_id")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except InvalidTokenError:
#         raise credentials_exception
    
    
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
    
#     return user

# @router.post("/login")
# async def login(  form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
# 	user = authenticate_user(fake_users_db, form_data.username, form_data.password)
# 	if not user:
# 		raise HTTPException(
# 			status_code=status.HTTP_401_UNAUTHORIZED,
# 			detail="Incorrect username or password",
# 		)
	
# 	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
# 	access_token = create_access_token(
# 		data={"user_id": user.username}, expires_delta=access_token_expires
# 	)
# 	return Token(access_token=access_token, token_type="bearer")


# @router.get("/auth", response_model=User)
# async def authUser(
#     current_user: Annotated[User, Depends(authorizate)],
# ):
#     return current_user
