#  uvicorn app.main:app --reload
#  fastapi dev app/main.py

from fastapi import FastAPI

from app import config
from app.logger import logger

app = FastAPI()

if app.debug:
    app.debug = True
else:
    app.debug = False


@app.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Wow! FastAPI is running!"}


@app.get("db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")


# новый маршрут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is  read_custom_message()"}


# Добавим тестовый endpoint для проверки
@app.get("/health")
def health_check():
    return {"status": "OK", "message": "FastAPI is working"}
