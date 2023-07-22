import math

import pandas as pd

from data.onet.loader.utils import parse_date, parse_int, parse_boolean, load_csv, load_document
from data.onet.models.occupation import *


def get_metadata(row: pd.Series):
    return Metadata(
        item=row['Item'],
        response=row['Response'],
        n=parse_int(row['N']),
        percent=row['Percent'],
        date_updated=parse_date(row['Date'])
    )


def get_technology_skill(row: pd.Series):
    return TechnologySkill(
        example=row['Example'],
        commodity_code=row['Commodity Code'],
        hot_technology=row['Commodity Title'],
        in_demand=row['Hot Technology']
    )


def get_tool(row: pd.Series):
    return Tool(
        example=row['Example'],
        commodity_code=row['Commodity Code']
    )


def get_emerging_task(row: pd.Series):
    return EmergingTask(
        task=row['Task'],
        category=row['Category'],
        original_task_id=parse_int(row['Original Task ID']),
        write_in_total=row['Write-in Total'],
        date_updated=parse_date(row['Date']),
        domain_source=row['Domain Source']
    )


def get_related_occupation(row: pd.Series):
    return RelatedOccupation(
        related_onetsoc_code=row['Related O*NET-SOC Code'],
        relatedness_tier=row['Relatedness Tier'],
        related_index=row['Index']
    )


def get_single_rating_base(row: pd.Series, wrap=True):
    mapping = {
        'element_id': row['Element ID'],
        'scale_id': row['Scale ID'],
        'data_value': row['Data Value'],
        'date_updated': parse_date(row['Date']),
        'domain_source': row['Domain Source']
    }
    if wrap:
        return SingleRatingBase(**mapping)
    return mapping


def get_multi_rating_base(row: pd.Series, wrap=True):
    mapping = {
        **get_single_rating_base(row, wrap=False),
        'n': parse_int(row['N']),
        'standard_error': row['Standard Error'],
        'lower_ci_bound': row['Lower CI Bound'],
        'upper_ci_bound': row['Upper CI Bound'],
        'recommend_suppress': parse_boolean(row['Recommend Suppress']),
    }
    if wrap:
        return MultiRatingBase(**mapping)
    return mapping


def get_work_context(row: pd.Series, wrap=True):
    mapping = {
        **get_multi_rating_base(row, wrap=False),
        'category': parse_int(row['Category']),
    }
    if wrap:
        return WorkContext(**mapping)
    return mapping


def get_task(row: pd.Series):
    return Task(
        task_id=row['Task ID'],
        task=row['Task'],
        dwa_ids=[],
        ratings=[],
        task_type=row['Task Type'],
        incumbents_responding=parse_int(row['Incumbents Responding']),
        date_updated=parse_date(row['Date']),
        domain_source=row['Domain Source']
    )


def get_task_rating(row: pd.Series):
    return TaskRating(
        scale_id=row['Scale ID'],
        category=parse_int(row['Category']),
        data_value=row['Data Value'],
        n=row['N'],
        standard_error=row['Standard Error'],
        lower_ci_bound=row['Lower CI Bound'],
        upper_ci_bound=row['Upper CI Bound'],
        recommend_suppress=parse_boolean(row['Recommend Suppress']),
        date_updated=parse_date(row['Date']),
        domain_source=row['Domain Source']
    )


async def load_content_model_reference():
    mapper = {'element_id': 'Element ID',
              'element_name': 'Element Name',
              'description': 'Description'}
    await load_document(ContentModelReference, mapper, 'Content Model Reference.txt')


async def load_occupation():
    result = dict()
    df = await load_csv('Occupation Data.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code] = Occupation(onetsoc_code=onetsoc_code, title=row['Title'], description=row['Description'])

    df = await load_csv('Alternate Titles.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        if (title := row['Alternate Title']) is not None:
            if isinstance(title, str):
                result[onetsoc_code].alternate_titles.append(title)
        if (title := row['Short Title']) is not None:
            if isinstance(title, str):
                result[onetsoc_code].alternate_titles.append(title)

    df = await load_csv('Sample of Reported Titles.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].reported_titles.append(row['Reported Job Title'])

    df = await load_csv('Job Zones.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].job_zone = row['Job Zone']

    df = await load_csv('Occupation Level Metadata.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].metadata.append(get_metadata(row))

    df = await load_csv('Abilities.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].abilities.append(get_multi_rating_base(row))

    df = await load_csv('Education, Training, and Experience.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].education_training_experience.append(get_multi_rating_base(row))

    df = await load_csv('Emerging Tasks.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].emerging_tasks.append(get_emerging_task(row))

    df = await load_csv('Interests.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].interests.append(get_single_rating_base(row))

    df = await load_csv('Knowledge.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].knowledge.append(get_multi_rating_base(row))

    df = await load_csv('Related Occupations.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].related_occupations.append(get_related_occupation(row))

    df = await load_csv('Skills.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].skills.append(get_multi_rating_base(row))

    df = await load_csv('Technology Skills.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].technology_skills.append(get_technology_skill(row))

    df = await load_csv('Tools Used.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].tools_used.append(get_tool(row))

    df = await load_csv('Work Activities.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].work_activities.append(get_multi_rating_base(row))

    df = await load_csv('Work Context.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].work_contexts.append(get_work_context(row))

    df = await load_csv('Work Styles.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].work_styles.append(get_multi_rating_base(row))

    df = await load_csv('Work Values.txt')
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        result[onetsoc_code].work_values.append(get_single_rating_base(row))

    df = await load_csv('Task Statements.txt')
    task_id_map = dict()
    for _, row in df.iterrows():
        onetsoc_code = row['O*NET-SOC Code']
        task = get_task(row)
        task_id_map[task.task_id] = task
        result[onetsoc_code].tasks.append(task)

    df = await load_csv('Tasks to DWAs.txt')
    for _, row in df.iterrows():
        task_id = row['Task ID']
        task_id_map[task_id].dwa_ids.append(row['DWA ID'])

    df = await load_csv('Task Ratings.txt')
    for _, row in df.iterrows():
        task_id = row['Task ID']
        task_id_map[task_id].ratings.append(get_task_rating(row))

    await Occupation.insert_many(list(result.values()))
