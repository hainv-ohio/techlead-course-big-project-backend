from .base import BaseStoreUsecase


class GetRevenueByDayUsecase(BaseStoreUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, start_date=None, end_date=None):
        return await self.repository.get_revenue_by_day(start_date, end_date)
