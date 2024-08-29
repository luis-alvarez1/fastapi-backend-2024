
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la Base de datos
DATABASE_URL = "mariadb+pymysql://animals_burnfeltat:aa0536c2106ff7272f86b688f2bd57742230f1b4@mku.h.filess.io:3305/animals_burnfeltat"

# Crea la conexión con la BD
engine = create_engine(
    DATABASE_URL
)

# Referencia a nuestra sesión de conexión con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Esta va a ser la base con la que vamos a crear las tablas en la db
Base = declarative_base()