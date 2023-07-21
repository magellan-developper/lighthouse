from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.state.mongodb = AsyncIOMotorClient('mongodb://localhost:27017')


@app.on_event("shutdown")
async def shutdown_event():
    app.state.mongodb.close()


async def get_db(request: Request):
    return request.app.state.mongodb


@app.get("/items/{item_id}")
async def read_item(item_id: str, db=Depends(get_db)):
    document = await db['mydb']['mycollection'].find_one({"_id": item_id})
    return {"item_id": item_id, "payload": document}
