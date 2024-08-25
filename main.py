from fastapi import FastAPI
from routers import animals

app = FastAPI()

app.include_router(animals.router)