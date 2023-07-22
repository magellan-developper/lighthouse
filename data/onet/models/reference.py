from beanie import Document, Indexed


# work context category, ete category
class ContextCategory(Document):
    element_id: Indexed(str)
    scale_id: str
    category: int
    category_description: str


class UNSPSC(Document):
    commodity_code: Indexed(str)
    commodity_title: str
    class_code: int
    class_title: str
    family_code: int
    family_title: str
    segment_code: int
    segment_title: str


class DWA(Document):
    element_id: str
    iwa_id: str
    dwa_id: str
    dwa_title: str


class IWA(Document):
    element_id: str
    iwa_id: str
    iwa_title: str


class LevelScaleAnchor(Document):
    element_id: str
    scale_id: str
    anchor_value: int
    anchor_description: str


class JobZoneReference(Document):
    job_zone: Indexed(int)
    name: str
    experience: str
    education: str
    job_training: str
    examples: str
    svp_range: str


class TaskCategory(Document):
    scale_id: str
    category: int
    category_description: str


class RIASECKeywords(Document):
    element_id: str
    keyword: str
    keyword_type: str


class ScalesReference(Document):
    scale_id: Indexed(str)
    scale_name: str
    minimum: int
    maximum: int
