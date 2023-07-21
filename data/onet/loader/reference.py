from data.onet.loader.utils import load_csv, load_document
from data.onet.models.reference import UNSPSC, DWA, IWA, RIASECKeywords, LevelScaleAnchor, ScalesReference


async def load_unspsc():
    mapper = {'commodity_code': 'Commodity Code',
              'commodity_title': 'Commodity Title',
              'class_code': 'Class Code',
              'class_title': 'Class Title',
              'family_code': 'Family Code',
              'family_title': 'Family Title',
              'segment_code': 'Segment Code',
              'segment_title': 'Segment Title'}
    await load_document(UNSPSC, mapper, 'UNSPSC Reference.txt')


async def load_dwa_reference():
    mapper = {'element_id': 'Element ID',
              'iwa_id': 'IWA ID',
              'dwa_id': 'DWA ID',
              'dwa_title': 'DWA Title'}
    await load_document(DWA, mapper, 'DWA Reference.txt')


async def load_iwa_reference():
    mapper = {'element_id': 'Element ID',
              'iwa_id': 'IWA ID',
              'iwa_title': 'IWA Title'}
    await load_document(IWA, mapper, 'IWA Reference.txt')


def load_riasec_keywords():
    mapper = {'element_id': 'Element ID',
              'iwa_id':  'IWA ID',
              'keyword': 'Keyword',
              'keyword_type':  'Keyword Type'}
    await load_document(RIASECKeywords, mapper, 'RIASEC Keywords.txt')


def load_level_scale_anchors():
    mapper = {'element_id': 'Element ID',
              'scale_id': 'Scale ID',
              'anchor_value': 'Anchor Value',
              'anchor_description': 'Anchor Description'}
    await load_document(LevelScaleAnchor, mapper, 'Level Scale Anchors.txt')

def load_scales_reference():
    mapper = {'scale_id': 'Scale ID',
              'scale_name': 'Scale Name',
              'minimum': 'Minimum',
              'maximum': 'Maximum'}
    await load_document(ScalesReference, mapper, 'Scales Reference.txt')


class ContextCategory(Document):
    element_id: str
    category: int
    category_description: str

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
