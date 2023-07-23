from fastapi import APIRouter

from app.utils.query import get_all_content_reference

router = APIRouter(prefix='/api/requirements/knowledge')


@router.get('/')
async def get_all_knowledge(prefix: str | None = None, limit: int = 10):
    return await get_all_content_reference('^2.C', prefix, limit)

