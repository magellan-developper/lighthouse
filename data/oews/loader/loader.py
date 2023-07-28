from data.onet.models.mapping import *
from data.oews.loader.mapping import *

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import asyncio


async def load_mapping():
    await load_job_salary()


async def load_oews_data():
    client = AsyncIOMotorClient('mongodb+srv://uofteceelcano:Dd8TbR5VaPkzuFVU@elcanocluster.bwllguc.mongodb.net/?retryWrites=true&w=majority')
    await init_beanie(database=client['lighthouse'], document_models=[Mapping])

    await load_mapping()


if __name__ == "__main__":
    asyncio.run(load_oews_data())
