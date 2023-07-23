from fastapi import APIRouter

from app.utils.query import get_all_content_reference

router = APIRouter(prefix='/api/characteristics/worker/work_styles')


@router.get('/')
async def get_all_work_styles(prefix: str | None = None, limit: int = 10):
    return await get_all_content_reference('^1.C', prefix, limit)
