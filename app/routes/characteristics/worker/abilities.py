from fastapi import APIRouter

from app.utils.query import get_all_content_reference

router = APIRouter(prefix='/api/characteristics/worker/abilities')


@router.get('/')
async def get_all_abilities(prefix: str | None = None, limit: int = 10):
    return await get_all_content_reference('^1.A', prefix, limit)
