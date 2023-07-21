import io
import urllib.parse

import aiohttp
import pandas as pd


async def load_csv(url, sep='\t'):
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            with io.StringIO(await response.text()) as text_io:
                return pd.read_csv(text_io, sep=sep)


async def load_document(document_type, params: dict, file_name: str):
    url = f'https://www.onetcenter.org/dl_files/database/db_26_3_text/{urllib.parse.quote(file_name)}'
    df = await load_csv(url)
    items = [document_type(**{k: row[v] for k, v in params.items()}) for _, row in df.iterrows()]
    await document_type.insert_many(items)
