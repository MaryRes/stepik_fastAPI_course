from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


# Создаем модель для входных данных
class NumberInput(BaseModel):
    number_1: float
    number_2: float


@app.get("/")
async def root():
    return {"message": "Go to /docs to test the calculator"}


@app.post("/add_numbers")
async def add_numbers(input_data: NumberInput):
    result = input_data.number_1 + input_data.number_2
    return {"result": result}
