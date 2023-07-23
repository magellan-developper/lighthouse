from fastapi import APIRouter

from app.utils.query import get_all_content_reference

router = APIRouter(prefix='/api/characteristics/worker/interests')


@router.get('/basic')
async def get_all_basic_interests(prefix: str | None = None, limit: int = 10):
    return await get_all_content_reference('^1.B.3', prefix, limit)


@router.get('/general')
async def get_all_general_interests(prefix: str | None = None, limit: int = 10):
    return await get_all_content_reference('^1.B.1', prefix, limit)
