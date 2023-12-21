import uvicorn
from fastapi import FastAPI
from typing import List
from src.services import get_users_mongo, sync_users
from src.responses import UsersItem

app = FastAPI()


@app.get("/users", response_model=List[UsersItem])
def get_user_routes():
    return get_users_mongo()


if __name__ == '__main__':
    users = get_users_mongo()

    if not users:
        sync_users()

    uvicorn.run(app, host="0.0.0.0", port=8000)
