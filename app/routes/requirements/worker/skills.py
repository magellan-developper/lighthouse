from typing import Optional

from fastapi import APIRouter

from app.utils.query import get_all_content_reference

router = APIRouter(prefix='/api/requirements/skills')


@router.get('/basic')
async def get_all_basic_skills(prefix: Optional[str] = None, limit: int = 10):
    return await get_all_content_reference('^2.A', prefix, limit)


@router.get('/cross_functional')
async def get_all_cross_functional_skills(prefix: Optional[str] = None, limit: int = 10):
    return await get_all_content_reference('^2.B', prefix, limit)
