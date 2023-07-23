from beanie import Document, Indexed


# work context category, ete category
class ContextCategory(Document):
    class Settings:
        name = "context_category"

    element_id: Indexed(str)
    scale_id: str
    category: int
    category_description: str


class UNSPSC(Document):
    class Settings:
        name = "unspsc"

    commodity_code: Indexed(str)
    commodity_title: str
    class_code: int
    class_title: str
    family_code: int
    family_title: str
    segment_code: int
    segment_title: str


class DWA(Document):
    class Settings:
        name = "dwa"

    element_id: str
    iwa_id: str
    dwa_id: str
    dwa_title: str


class IWA(Document):
    class Settings:
        name = "iwa"

    element_id: str
    iwa_id: str
    iwa_title: str


class LevelScaleAnchor(Document):
    class Settings:
        name = "level_scale_anchor"

    element_id: str
    scale_id: str
    anchor_value: int
    anchor_description: str


class JobZoneReference(Document):
    class Settings:
        name = "job_zone_reference"

    job_zone: Indexed(int)
    name: str
    experience: str
    education: str
    job_training: str
    examples: str
    svp_range: str


class TaskCategory(Document):
    class Settings:
        name = "task_category"

    scale_id: str
    category: int
    category_description: str


class RIASECKeywords(Document):
    class Settings:
        name = "riasec_keywords"

    element_id: str
    keyword: str
    keyword_type: str


class ScalesReference(Document):
    class Settings:
        name = "scales_reference"

    scale_id: Indexed(str)
    scale_name: str
    minimum: int
    maximum: int


def get_reference_models():
    return [ContextCategory, JobZoneReference, TaskCategory,
            ScalesReference, UNSPSC, DWA, IWA, RIASECKeywords, LevelScaleAnchor]
