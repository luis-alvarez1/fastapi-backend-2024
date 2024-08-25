from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine
 

animal = Table("animals", meta, 
               Column("id", Integer, primary_key=True),
               Column("name", String(255)),
               Column("age", Integer),
               Column("habitad", String(255))
               )

meta.create_all(engine)