from data.onet.loader.mapping import *
from data.onet.loader.reference import *
from data.onet.loader.occupation import *

from data.onet.models.occupation import *
from data.onet.models.reference import *

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import asyncio


async def load_references():
    await load_unspsc()
    await load_task_categories()
    await load_dwa_reference()
    await load_iwa_reference()
    await load_riasec_keywords()
    await load_level_scale_anchors()
    await load_scales_reference()
    await load_job_zone_reference()
    await load_context_categories()


async def load_mapping():
    await load_element_mapping()
    await load_interest_mapping()


async def load_onet_data():
    client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")
    await init_beanie(database=client['lighthouse'],
                      document_models=[InterestMapping, Mapping, Occupation, ContentModelReference,
                                       ContextCategory, JobZoneReference, TaskCategory,
                                       ScalesReference, UNSPSC, DWA, IWA, RIASECKeywords, LevelScaleAnchor])

    await load_occupation()
    await load_content_model_reference()
    await load_mapping()
    await load_references()


if __name__ == "__main__":
    asyncio.run(load_onet_data())
