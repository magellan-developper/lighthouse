
from data.onet.loader.utils import load_document
from data.onet.models.mapping import Mapping, InterestMapping

async def load_document(document_type, params: dict, file_name: str):
    url = f'https://www.onetcenter.org/dl_files/database/db_26_3_text/{urllib.parse.quote(file_name)}'
    df = await load_csv(url)
    items = [document_type(**{k: row[v] for k, v in params.items()}) for _, row in df.iterrows()]
    await document_type.insert_many(items)
async def load_mapping():
    mapper = {'element_id', 'Abilities Element ID',
              '':'Work Context Element ID',
                '':'Abilities Element Name',
                '':'Abilities Element Name'}
    'Abilities to Work Context.txt'

class Mapping(Document):
    element_id: Indexed(str)
    targets: list[str]


class InterestMapping(Document):
    element_id: str
    interest_type: str
    mapped_type: str  # occupation / activity
    content: str  # onetsoc_code / activity
