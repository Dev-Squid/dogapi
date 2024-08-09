from fastapi import FastAPI

from . import models
from .config import settings
from .database import engine
from . routers import dogs, users, auth, comments, votes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(dogs.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(comments.router)
app.include_router(votes.router)