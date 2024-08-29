from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

# Heredamos la clase de Base para decirle al ORM que queremos crear una tabla
class Animal(Base):
    # Este es el nombre con el que se va a crear la tabla
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    habitad = Column(String(255))
    age = Column(Integer, default=0)
    type = Column(String(255))



