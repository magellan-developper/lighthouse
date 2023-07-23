from fastapi import APIRouter
from pydantic import BaseModel
from data.onet.models.occupation import Occupation

router = APIRouter(prefix='/api/interests')

