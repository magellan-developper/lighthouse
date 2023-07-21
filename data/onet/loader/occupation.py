import sqlite3
from sqlite3 import Error

from data.onet.loader.utils import load_document
from data.onet.models.occupation import ContentModelReference


def load_content_model_reference():
    mapper = {'element_id': 'Element ID',
              'element_name': 'Element Name',
              'description': 'Description'}
    await load_document(ContentModelReference, mapper, 'Content Model Reference.txt')

def load_occupation():
    result = {

    }

    class Occupation(Document):
        onetsoc_code: Indexed(str)
        title: Title
        alternate_titles: list[str]
        metadata: list[Metadata]
        abilities: list[MultiRatingBase]
        education_training_experience: list[MultiRatingBase]
        emerging_tasks: list[EmergingTask]
        interests: list[SingleRatingBase]
        job_zone: int
        knowledge: list[MultiRatingBase]
        related_occupations: list[RelatedOccupation]
        skills: list[MultiRatingBase]
        tasks: list[Task]
        tools_used: list[Tool]
        technology_skills: list[TechnologySkill]
        work_activities: list[MultiRatingBase]
        work_styles: list[MultiRatingBase]
        work_values: list[SingleRatingBase]