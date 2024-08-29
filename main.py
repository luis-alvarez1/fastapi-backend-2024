from fastapi import FastAPI, Request
from routers.users import users
from routers.animals import animals
from models import animal
from config.db import engine
import time


animal.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.middleware("http")
async def add_process_time_header(req: Request, call_next):
	start_time = time.time()
	response = await call_next(req)
	process_time = time.time() - start_time
	response.headers["X-Process-Time"] = str(process_time)
	return response

app.include_router(animals.router)
app.include_router(users.router)