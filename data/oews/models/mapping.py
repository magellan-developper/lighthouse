from beanie import Document
from typing import Optional

class Mapping(Document):
    class Settings:
        name = "job_salary"

    src_element_id: str
    job_title: str
    hourly_salary: Optional[float]
    annual_salary: Optional[int]
    hourly_median: Optional[float]
    annual_median: Optional[int]
    total_employment: Optional[int]
    

def get_mapping_models():
    return [Mapping]
