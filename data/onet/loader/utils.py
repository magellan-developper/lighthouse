import io
import math
import urllib.parse
from datetime import datetime
from typing import Optional

import aiohttp
import pandas as pd


def parse_date(item):
    if '/' in item:  # month format
        return datetime.strptime(item, '%m/%Y')
    return datetime.strptime(item, '%Y-%m-%d')


def parse_int(item):
    if item is None or math.isnan(item):
        return None
    return int(item)


def parse_boolean(item):
    if item == 'Y':
        return True
    elif item == 'N':
        return False
    elif math.isnan(item):
        return None
    return item


async def load_csv(file_name: str, sep: str = '\t'):
    url = f'https://www.onetcenter.org/dl_files/database/db_27_3_text/{urllib.parse.quote(file_name)}'
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            with io.StringIO(await response.text()) as text_io:
                return pd.read_csv(text_io, sep=sep)


async def load_document(document_type, params: dict, file_name: str):
    df = await load_csv(file_name)
    items = [document_type(**{k: row[v] for k, v in params.items()}) for _, row in df.iterrows()]
    await document_type.insert_many(items)
