from fastapi import APIRouter
from pydantic import BaseModel
from data.onet.models.occupation import Occupation

router = APIRouter(prefix='/api/occupations')


class OccupationProjection(BaseModel):
    onetsoc_code: str
    title: str
    description: str


class RelatedOccupationProjection(BaseModel):
    related_occupations: list


@router.get('/')
async def get_all_occupations(prefix: Optional[str] = None, limit: int = 10):
    if prefix is not None:
        query = Occupation.find_many({"$text": {"$search": prefix}})
    else:
        query = Occupation.find_all()
    return await query.limit(limit).project(OccupationProjection).to_list()


@router.get('/detail/{onetsoc_code}')
async def get_occupation_detail(onetsoc_code: str):
    return await Occupation.find(Occupation.onetsoc_code == onetsoc_code).first_or_none()


@router.get('/related/{onetsoc_code}')
async def get_related_occupations(onetsoc_code: str):
    occupation = Occupation.find(Occupation.onetsoc_code == onetsoc_code).project(RelatedOccupationProjection)
    return await occupation.first_or_none()


@router.get('/interests/{onetsoc_code}')
async def get_occupation_interests(onetsoc_code):
    results = await Occupation.find(Occupation.onetsoc_code == onetsoc_code).aggregate([
        {
            '$project': {
                'onetsoc_code': 1,
                'title': 1,
                'interests': 1
            }
        }, {
            '$lookup': {
                'from': 'content_model_reference',
                'localField': 'interests.element_id',
                'foreignField': 'element_id',
                'as': 'details'
            }
        }, {
            '$project': {
                '_id': 0,
                'onetsoc_code': 1,
                'title': 1,
                'scale_id': '$interests.scale_id',
                'value': '$interests.data_value',
                'element_id': '$interests.element_id',
                'element_name': '$details.element_name',
                'description': '$details.description'
            }
        }
    ]).to_list()
    result = results[0]
    result = {'onetsoc_code': result['onetsoc_code'],
              'title': result['title'],
              'interests': [
                  {'scale_id': scale_id,
                   'value': value,
                   'element_id': element_id,
                   'element_name': element_name,
                   'description': description}
                  for scale_id, value, element_id, element_name, description in
                  zip(result['scale_id'],
                      result['value'],
                      result['element_id'],
                      result['element_name'],
                      result['description'])
              ]}
    return result
