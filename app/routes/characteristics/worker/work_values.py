from typing import Optional

from fastapi import APIRouter

from app.utils.query import get_all_content_reference

router = APIRouter(prefix='/api/characteristics/worker/work_values')


@router.get('/')
async def get_all_work_values(prefix: Optional[str] = None, limit: int = 10):
    return await get_all_content_reference('^1.B.2', prefix, limit)