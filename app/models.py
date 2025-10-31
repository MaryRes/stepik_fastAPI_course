from datetime import datetime

from pydantic import BaseModel


# Создаём модель данных, которая обычно располагается в файле models.py
class User(BaseModel):
    id: int
    signup_ts: datetime | None = None
    friends: list[int] = []


# Внешние данные, имитирующие входящий JSON
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

# Имитация распаковки входящих данных в коде приложения
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]

print(user.id)  # 123
print(user.signup_ts)  # 2017-06-01 12:22:


class User(BaseModel):
    username: str
    message: str


# Пример FastAPI приложения, использующего модель User
from fastapi import FastAPI

app_2 = FastAPI()


@app_2.post("/")
async def root(user: User):
    """
    Здесь мы можем с переменной user, которая содержит объект класса User с соответствующими полями,
    выполнить любую логику – например, сохранить информацию в базу данных, передать в другую функцию и т.д.
    """
    print(f"Мы получили от юзера {user.username} такое сообщение: {user.message}")
    return user
