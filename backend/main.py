
from typing import Union
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class Person(BaseModel):
    id: int
    name: str
    age: int


DB: List[Person] = [
    Person(id=1, name="Jamila", age=22),
    Person(id=2, name="Alex", age=18),
    Person(id=3, name="Ali", age=15)

]


@app.get("/api")
def read_root():
    return DB


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
