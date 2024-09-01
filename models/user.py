from config.db import Base
from sqlalchemy import Column, String, Integer

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	username = Column(String(255))
	email = Column(String(255))
	password = Column(String(255))