import pytest

from unittest.mock import MagicMock

from kink import di

from services.item_management.domain.entities.item import Item
from services.item_management.domain.repository import ItemRepository
from services.item_management.domain.usecases import UpdateItemUseCase
from core.types.failure import Failure

class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)

@pytest.mark.asyncio
async def test_update_item_success():

    itemUpdate = Item(
        id = 9,
        name = "item_test_update",
        category_id = 9,
        price = '20000',
        currency_code = 1,
        detail = "detail test_update"
    )

    mock_repository = ItemRepository()

    mock_repository.update_item = AsyncMock(
        return_value=(
            Item(
                id=itemUpdate.id,
                name=itemUpdate.name, 
                category_id=itemUpdate.category_id, 
                price=itemUpdate.price,
                currency_code=itemUpdate.currency_code,
                detail=itemUpdate.detail
            ), None)
    )

    di[ItemRepository] = mock_repository

    usecase = UpdateItemUseCase()

    item, failure = await usecase.execute(itemUpdate)

    mock_repository.update_item.assert_called_once_with(itemUpdate)

    # Assert it return expected Success results + registered User
    assert failure is None
    assert item.id == itemUpdate.id
    assert item.name == itemUpdate.name
    assert item.category_id == itemUpdate.category_id
    assert item.price == itemUpdate.price
    assert item.currency_code == itemUpdate.currency_code
    assert item.detail == itemUpdate.detail