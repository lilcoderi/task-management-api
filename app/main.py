from fastapi import FastAPI
from app import models, database, routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Task Management API",
    description="API for managing tasks with CRUD, filtering, and sorting, built with **FastAPI** and **MySQL**.",
    version="1.0.0"
)

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Management API"}
