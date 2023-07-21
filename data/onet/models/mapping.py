from datetime import datetime
from typing import Optional

from beanie import Document, Indexed
from pydantic import BaseModel


class Mapping(Document):
    element_id: Indexed(str)
    targets: list[str]


class InterestMapping(Document):
    element_id: str
    interest_type: str
    mapped_type: str  # occupation / activity
    content: str  # onetsoc_code / activity
