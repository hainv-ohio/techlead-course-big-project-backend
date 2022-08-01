import pytest

from unittest.mock import MagicMock

from kink import di

from services.item_management.domain.entities.item import Item
from services.item_management.domain.repository import ItemRepository
from services.item_management.domain.usecases import GetItemUseCase
from core.types.failure import Failure


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)

@pytest.mark.asyncio
async def test_get_item_success():

    item_id = 1
    name = "item_test"
    category_id = 2
    price = '20000'
    currency_code = 1
    detail = "detail test"

    mock_repository = ItemRepository()

    mock_repository.get_item_by_id = AsyncMock(
        return_value=(
            Item(
                id=item_id,
                name=name, 
                category_id=category_id, 
                price=price,
                currency_code=currency_code,
                detail=detail
            ), None)
    )

    di[ItemRepository] = mock_repository

    usecase = GetItemUseCase()

    item, failure = await usecase.execute(
        id=item_id)

    mock_repository.get_item_by_id.assert_called_once_with(
        id=item_id
    )
    # Assert it return expected Success results + registered User
    assert failure is None
    assert item.id == item_id