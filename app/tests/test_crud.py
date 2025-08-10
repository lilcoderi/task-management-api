import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from app import crud, schemas
from app.database import Base

# Load environment variables from .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Engine and Session for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db_session():
    """Fixture untuk membuat session yang aman, tanpa hapus tabel atau data lama."""
    connection = engine.connect()
    transaction = connection.begin() 

    db = TestingSessionLocal(bind=connection)
    try:
        yield db
    finally:
        db.rollback()
        connection.close()
        transaction.rollback()

def test_create_task(db_session):
    task_data = schemas.TaskCreate(
        title="Test Task",
        description="This is a test",
        category="Work",
        priority="High",
        deadline="2025-08-20"
    )
    task = crud.create_task(db_session, task_data)
    assert task.id is not None
    assert task.title == "Test Task"

def test_get_tasks(db_session):
    task_data = schemas.TaskCreate(
        title="Another Task",
        description="Test filter",
        category="Personal",
        priority="Low",
        deadline="2025-08-25"
    )
    crud.create_task(db_session, task_data)
    tasks = crud.get_tasks(db_session)
    assert len(tasks) >= 1

def test_get_task(db_session):
    task_data = schemas.TaskCreate(
        title="Find Me",
        description="Testing get by ID",
        category="Work",
        priority="Medium",
        deadline="2025-09-01"
    )
    created = crud.create_task(db_session, task_data)
    found = crud.get_task(db_session, created.id)
    assert found is not None
    assert found.title == "Find Me"

def test_update_task(db_session):
    task_data = schemas.TaskCreate(
        title="Old Title",
        description="Before update",
        category="Work",
        priority="Medium",
        deadline="2025-09-01"
    )
    created = crud.create_task(db_session, task_data)
    update_data = schemas.TaskUpdate(
        title="New Title",
        description="After update",
        category="Work",
        priority="High",
        deadline="2025-09-05"
    )
    updated = crud.update_task(db_session, created.id, update_data)
    assert updated.title == "New Title"
    assert updated.priority == "High"

def test_delete_task(db_session):
    task_data = schemas.TaskCreate(
        title="Delete Me",
        description="To be deleted",
        category="Work",
        priority="Low",
        deadline="2025-09-10"
    )
    created = crud.create_task(db_session, task_data)
    deleted = crud.delete_task(db_session, created.id)
    assert deleted is not None
    assert crud.get_task(db_session, created.id) is None
