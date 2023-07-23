from fastapi import FastAPI
from app.routes import occupation
from data.database import init_db

import uvicorn

app = FastAPI()
app.include_router(occupation.router)


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get('/')
def home():
    return {'message': 'Home Page'}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
