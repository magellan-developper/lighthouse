from datetime import datetime
from typing import Optional

import pymongo
from beanie import Document, Indexed
from pydantic import BaseModel


class Title(BaseModel):
    title: str
    description: str


class ElementBase(BaseModel):
    element_id: str
    scale_id: str


class SingleRatingBase(ElementBase):
    data_value: float
    date_updated: datetime
    domain_source: str


class MultiRatingBase(SingleRatingBase):
    n: Optional[float]
    standard_error: Optional[float]
    lower_ci_bound: Optional[float]
    upper_ci_bound: Optional[float]
    recommend_suppress: Optional[bool]


class Metadata(BaseModel):
    item: str
    response: Optional[str]
    n: Optional[int]
    percent: Optional[float]
    date_updated: datetime


class TaskRating(BaseModel):
    scale_id: str
    category: Optional[int]
    data_value: float
    n: Optional[float]
    standard_error: Optional[float]
    lower_ci_bound: Optional[float]
    upper_ci_bound: Optional[float]
    recommend_suppress: Optional[str]
    date_updated: datetime
    domain_source: str


class Task(BaseModel):
    task_id: int
    task: str
    dwa_ids: list[str]
    ratings: list[TaskRating]
    task_type: Optional[str]
    incumbents_responding: Optional[int]
    date_updated: datetime
    domain_source: str


class TechnologySkill(BaseModel):
    example: str
    commodity_code: str
    hot_technology: str
    in_demand: bool


class WorkContext(MultiRatingBase):
    category: Optional[int]


class Tool(BaseModel):
    example: str
    commodity_code: str  # UNSPSC


class EmergingTask(BaseModel):
    task: str
    category: str
    original_task_id: Optional[int]
    write_in_total: int
    date_updated: datetime
    domain_source: str


class RelatedOccupation(BaseModel):
    related_onetsoc_code: str
    relatedness_tier: str
    related_index: int


class Occupation(Document):
    class Settings:
        name = "occupation"
        indexes = [
            ('title', pymongo.TEXT),
            ('description', pymongo.TEXT)
        ]

    onetsoc_code: Indexed(str)
    title: str
    description: str
    alternate_titles: list[str] = []
    reported_titles: list[str] = []
    metadata: list[Metadata] = []
    abilities: list[MultiRatingBase] = []
    education_training_experience: list[MultiRatingBase] = []
    emerging_tasks: list[EmergingTask] = []
    interests: list[SingleRatingBase] = []
    job_zone: Optional[int] = None
    knowledge: list[MultiRatingBase] = []
    related_occupations: list[RelatedOccupation] = []
    skills: list[MultiRatingBase] = []
    tasks: list[Task] = []
    tools_used: list[Tool] = []
    technology_skills: list[TechnologySkill] = []
    work_activities: list[MultiRatingBase] = []
    work_contexts: list[WorkContext] = []
    work_styles: list[MultiRatingBase] = []
    work_values: list[SingleRatingBase] = []


class ContentModelReference(Document):
    class Settings:
        name = "content_model_reference"

    element_id: Indexed(str)
    element_name: str
    description: str


def get_occupation_models():
    return [ContentModelReference, Occupation]
