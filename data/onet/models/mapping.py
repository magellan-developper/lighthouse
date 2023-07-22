from beanie import Document


class Mapping(Document):
    src_element_id: str
    src_type: str
    target_element_id: str
    target_type: str


class InterestMapping(Document):
    element_id: str
    interest_type: str
    mapped_type: str  # occupation / activity
    content: str  # onetsoc_code / activity
