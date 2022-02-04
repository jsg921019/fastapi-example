from fastapi import FastAPI
from .routers import user, auth, post, vote
from fastapi.middleware.cors import CORSMiddleware

# from . import models
# from .database import engine
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for tag in [user, auth, post, vote]:
    app.include_router(tag.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}
