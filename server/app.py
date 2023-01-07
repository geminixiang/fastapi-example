import logging

import uvicorn
from model import UserModel
from pydantic import ValidationError
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from config.log_config import uvicorn_logger
from db.fake_db import db

try:
    # Logging
    # 1. .py
    # logging.config.dictConfig(uvicorn_logger)
    # 2. .yml
    import yaml
    with open('server/config/log_config.yml', 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)
except Exception:
    print("sudo touch /var/log/fast-test.log")
    print("sudo chmod 666 /var/log/fast-test.log")

NOT_EXIST = Response(status_code=400, content="not exists", media_type="text/event-stream")
def VALIDATION(msg):
    return JSONResponse(status_code=400, content={"msg": str(msg)})
origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:5000",
    "http://127.0.0.1:5500",
]

app = FastAPI(
    title="FastAPI example",
    description="This is a simple application of FastAPI",
    docs_url="/",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/v1/user")
async def user(v: str):
    """
    Simple GET db api
    """
    res, doc = contains(db, lambda x: x['username'] == v)
    if not res:
        return NOT_EXIST

    return JSONResponse(
        status_code=200,
        content=doc
    )


@app.put("/v1/user")
@app.post("/v1/user")
async def put_user(v: str, data: dict):
    """
    Simple POST db api
    """
    res, doc = contains(db, lambda x: x['username'] == v)
    if not res:
        return NOT_EXIST

    doc.update(data)

    try:
        UserModel(**doc)
    except ValidationError as e:
        return VALIDATION(e)

    return JSONResponse(
        status_code=200,
        content=doc
    )


def contains(list, filter):
    for x in list:
        if filter(x):
            return True, x
    return False, None


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000)
