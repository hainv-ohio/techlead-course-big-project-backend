from array import array
import sqlalchemy as sa
from core.base.base_dao import BaseDao
from ..orm import ItemORM


class ItemDAO(BaseDao):
    model = ItemORM

    async def findByIds(self, ids: array) -> ItemORM:
        statement = sa.select(self.model).filter(self.model.id.in_(ids))

        async with self.session_builder() as session:
            query_result = await session.execute(statement)
            results = query_result.unique().scalars().all()
        return results


