from typing import Optional

from fastapi import APIRouter

from app.utils.query import get_all_content_reference

router = APIRouter(prefix='/api/requirements/education')


@router.get('/')
async def get_all_education(prefix: Optional[str] = None, limit: int = 10):
    return await get_all_content_reference('^2.D', prefix, limit)

