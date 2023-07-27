from typing import Optional

from data.onet.models.occupation import ContentModelReference


async def get_all_content_reference(regex, prefix: Optional[str] = None, limit: int = 10):
    if prefix is not None:
        query = ContentModelReference.find_many({"$text": {"$search": prefix}})
    else:
        query = ContentModelReference.find_all()
    return await query.aggregate([
        {
            '$match': {
                'element_id': {
                    '$regex': regex
                }
            }
        },
        {
            '$limit': limit
        }
    ]).to_list()
