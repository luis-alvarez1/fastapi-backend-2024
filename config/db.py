
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mariadb+pymysql://animals_burnfeltat:aa0536c2106ff7272f86b688f2bd57742230f1b4@mku.h.filess.io:3305/animals_burnfeltat"

engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()