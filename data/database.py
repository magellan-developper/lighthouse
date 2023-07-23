from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from data.onet.models.mapping import get_mapping_models
from data.onet.models.reference import get_reference_models

from data.onet.models.occupation import get_occupation_models


async def init_db():
    client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")
    document_models = []
    document_models += get_occupation_models()
    document_models += get_reference_models()
    document_models += get_mapping_models()
    await init_beanie(database=client['lighthouse'], document_models=document_models)
