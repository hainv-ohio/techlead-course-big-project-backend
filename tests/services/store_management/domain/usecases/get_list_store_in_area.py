import unittest

from services.store_management.domain.usecases.get_list_store_by_area import GetListStoreByAreaUsecase


class TestGetListStoreInArea(unittest.TestCase):

    def __init__(self):
        self.get_list_store_by_area = GetListStoreByAreaUsecase()

    def get_list_store_by_area_id(self, area_id):
        return self.get_list_store_by_area.execute(area_id)

    def test_number_of_stores_in_hanoi(self):
        list_store_in_hanoi = self.get_list_store_by_area_id(29)
        self.assertEqual(len(list_store_in_hanoi), 3)

    def test_area_id_does_not_exist(self):
        list_store = self.get_list_store_by_area_id(9999)
        self.assertEqual(len(list_store), 0)

    def test_input_is_not_integer(self):
        with self.assertRaises(TypeError):
            self.get_list_store_by_area_id('test_string')


if __name__ == '__main__':
    unittest.main()
