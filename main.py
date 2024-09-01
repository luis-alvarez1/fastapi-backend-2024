from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from routers.users import users
from routers.animals import animals
from models import animal
from config.db import engine
from config.redis import redis
import time


'''
Creamos las tablas que estén pendientes por crear con:
	modelo.Base.metadata.create_all(bind=engine)
 
Así con las futuras tablas
'''
animal.Base.metadata.create_all(bind=engine)


app = FastAPI()


# @app.middleware("http")
# async def add_process_time_header(req: Request, call_next):
# 	start_time = time.time()
# 	response = await call_next(req)
# 	process_time = time.time() - start_time
# 	response.headers["X-Process-Time"] = str(process_time)
# 	return response

# @app.middleware("http")
# async def api_rate_limit(req: Request, call_next):
#     # limite de requests cada 3 segundos
# 	limit = 3
# 	# obtiene la ip del usuario
# 	ip = req.client.host
# 	# crea el registro incremental de la ip
# 	redis.incr(ip)
# 	# le aplica una expiración de 3 segundos
# 	redis.expire(ip, time=3)
# 	#obtiene el número de requests
# 	requests = int(redis.get(ip))
# 	# si el número de requests es mayor al límite -> 429
# 	if requests >= limit:
# 		return JSONResponse(status_code=status.HTTP_429_TOO_MANY_REQUESTS, content={ "detail": "Too many requests"})
# 	# sino pasa
# 	response = await call_next(req)
# 	return response

app.include_router(animals.router)
app.include_router(users.router)