import typing

from fastapi import FastAPI
from orjson import orjson
from starlette.responses import JSONResponse

from app.routes import occupation
from data.database import init_db

import uvicorn


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content)


app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(occupation.router)


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get('/')
def home():
    return {'message': 'Home Page'}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
