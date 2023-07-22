from data.onet.loader.utils import load_csv, load_document
from data.onet.models.reference import *


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


async def load_riasec_keywords():
    mapper = {'element_id': 'Element ID',
              'keyword': 'Keyword',
              'keyword_type': 'Keyword Type'}
    await load_document(RIASECKeywords, mapper, 'RIASEC Keywords.txt')


async def load_level_scale_anchors():
    mapper = {'element_id': 'Element ID',
              'scale_id': 'Scale ID',
              'anchor_value': 'Anchor Value',
              'anchor_description': 'Anchor Description'}
    await load_document(LevelScaleAnchor, mapper, 'Level Scale Anchors.txt')


async def load_scales_reference():
    mapper = {'scale_id': 'Scale ID',
              'scale_name': 'Scale Name',
              'minimum': 'Minimum',
              'maximum': 'Maximum'}
    await load_document(ScalesReference, mapper, 'Scales Reference.txt')


async def load_job_zone_reference():
    mapper = {'job_zone': 'Job Zone',
              'name': 'Name',
              'experience': 'Experience',
              'education': 'Education',
              'job_training': 'Job Training',
              'examples': 'Examples',
              'svp_range': 'SVP Range'}
    await load_document(JobZoneReference, mapper, 'Job Zone Reference.txt')


async def load_task_categories():
    mapper = {'scale_id': 'Scale ID',
              'category': 'Category',
              'category_description': 'Category Description'}
    await load_document(TaskCategory, mapper, 'Task Categories.txt')


async def load_context_categories():
    mapper = {'element_id': 'Element ID',
              'scale_id': 'Scale ID',
              'category': 'Category',
              'category_description': 'Category Description'}
    await load_document(ContextCategory, mapper, 'Education, Training, and Experience Categories.txt')
    await load_document(ContextCategory, mapper, 'Work Context Categories.txt')
