from data.onet.loader.utils import load_csv
from data.onet.models.mapping import *


async def load_element_mapping():
    df = await load_csv('Abilities to Work Activities.txt')
    items = []
    for _, row in df.iterrows():
        item = Mapping(
            src_element_id=row['Abilities Element ID'],
            src_type='ability',
            target_element_id=row['Work Activities Element ID'],
            target_type='work_activity')
        items.append(item)

    df = await load_csv('Abilities to Work Context.txt')
    for _, row in df.iterrows():
        item = Mapping(
            src_element_id=row['Abilities Element ID'],
            src_type='ability',
            target_element_id=row['Work Context Element ID'],
            target_type='work_context')
        items.append(item)

    df = await load_csv('Skills to Work Activities.txt')
    for _, row in df.iterrows():
        item = Mapping(
            src_element_id=row['Skills Element ID'],
            src_type='skill',
            target_element_id=row['Work Activities Element ID'],
            target_type='work_activity')
        items.append(item)

    df = await load_csv('Skills to Work Context.txt')
    for _, row in df.iterrows():
        item = Mapping(
            src_element_id=row['Skills Element ID'],
            src_type='skill',
            target_element_id=row['Work Context Element ID'],
            target_type='work_context')
        items.append(item)

    df = await load_csv('Basic Interests to RIASEC.txt')
    for _, row in df.iterrows():
        item = Mapping(
            src_element_id=row['Basic Interests Element ID'],
            src_type='basic_interest',
            target_element_id=row['RIASEC Element ID'],
            target_type='riasec')
        items.append(item)

    await Mapping.insert_many(items)


async def load_interest_mapping():
    df = await load_csv('Interests Illustrative Activities.txt')
    items = []
    for _, row in df.iterrows():
        item = InterestMapping(
            element_id=row['Element ID'],
            interest_type=row['Interest Type'],
            mapped_type='activity',
            content=row['Activity'])
        items.append(item)

    df = await load_csv('Interests Illustrative Occupations.txt')
    for _, row in df.iterrows():
        item = InterestMapping(
            element_id=row['Element ID'],
            interest_type=row['Interest Type'],
            mapped_type='occupation',
            content=row['O*NET-SOC Code'])
        items.append(item)
    await InterestMapping.insert_many(items)

