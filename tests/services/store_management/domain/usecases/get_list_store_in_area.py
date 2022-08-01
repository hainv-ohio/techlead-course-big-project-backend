import asyncio
import unittest
from datetime import date
from unittest.mock import MagicMock

from kink import di

from services.store_management.domain.entities.store import Store
from services.store_management.domain.repository import StoreRepository
from services.store_management.domain.usecases.get_list_store_by_area import GetListStoreByAreaUsecase


class TestGetListStoreInArea(unittest.TestCase):

    @asyncio.coroutine
    def test_number_of_stores_in_hanoi(self):
        # Set up
        mock_data = StoreRepository()
        mock_data.get_list_store_by_area = MagicMock(
            return_value=(
                {
                    Store(
                        store_id=1,
                        user_id=2,
                        device_id=2,
                        device_type='ios',
                        address_id=100,
                        created_at=date(2022, 7, 1),
                        updated_at=date(2022, 8, 1)
                    ),
                    Store(
                        store_id=2,
                        user_id=12,
                        device_id=12,
                        device_type='android',
                        address_id=101,
                        created_at=date(2022, 7, 1),
                        updated_at=date(2022, 8, 1)
                    ),
                    Store(
                        store_id=3,
                        user_id=100,
                        device_id=12,
                        device_type='ios',
                        address_id=110,
                        created_at=date(2022, 7, 1),
                        updated_at=date(2022, 8, 1)
                    )
                }
            )
        )

        di[StoreRepository] = mock_data
        usecase = GetListStoreByAreaUsecase()

        # Run
        list_store_in_hanoi, failure =  usecase.execute(29)

        # Assert
        self.assertEqual(len(list_store_in_hanoi), 5)

    @asyncio.coroutine
    def test_area_id_does_not_exist(self):
        # Set up
        mock_data = StoreRepository()
        mock_data.get_list_store_by_area = MagicMock(
            return_value=(
                {
                    Store(
                        store_id=1,
                        user_id=2,
                        device_id=2,
                        device_type='ios',
                        address_id=100,
                        created_at=date(2022, 7, 1),
                        updated_at=date(2022, 8, 1)
                    ),
                    Store(
                        store_id=2,
                        user_id=12,
                        device_id=12,
                        device_type='android',
                        address_id=101,
                        created_at=date(2022, 7, 1),
                        updated_at=date(2022, 8, 1)
                    ),
                    Store(
                        store_id=3,
                        user_id=100,
                        device_id=12,
                        device_type='ios',
                        address_id=110,
                        created_at=date(2022, 7, 1),
                        updated_at=date(2022, 8, 1)
                    )
                }
            )
        )

        di[StoreRepository] = mock_data
        usecase = GetListStoreByAreaUsecase()

        # Run
        list_store_in_hanoi, failure = usecase.execute('area_id')

        # Assert
        self.assertTrue(failure is None)
        self.assertEqual(failure.message, "Area id must is integer")
        self.assertEqual(failure.code, 500)


if __name__ == '__main__':
    unittest.main()
