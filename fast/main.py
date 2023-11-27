from multiprocessing import context
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return