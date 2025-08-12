from fastapi import FastAPI
from mangum import Mangum

from app.main import app 

handler = Mangum(app)