from sqlalchemy import create_engine, MetaData

engine = create_engine(
	"mariadb+pymysql://animals_burnfeltat:aa0536c2106ff7272f86b688f2bd57742230f1b4@mku.h.filess.io:3305/animals_burnfeltat", 
echo=True)

meta = MetaData()

conn = engine.connect()