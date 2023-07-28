import pandas as pd
from data.oews.models.mapping import *

async def load_job_salary():
    base = 'data/oews/raw_data/'
    df = pd.read_excel(base + 'oesm22all/all_data_M_2022.xlsx')
    df.replace(['*', '#', '**', '~'], None, inplace=True)

    items = []
    for _, row in df.iterrows():
        # there are repetitioins in the OCC_TITLE column with only different O_GROUP
        try:
            if row['OCC_TITLE'] == items[-1].job_title:
                continue
        except:
            pass
    
        item = Mapping(
            src_element_id=row['OCC_CODE'],
            job_title=row['OCC_TITLE'],
            hourly_salary=row['H_MEAN'],
            annual_salary=row['A_MEAN'],
            hourly_median=row['H_MEDIAN'],
            annual_median=row['A_MEDIAN'],
            total_employment=row['TOT_EMP']
        )
        items.append(item)

    await Mapping.insert_many(items)
