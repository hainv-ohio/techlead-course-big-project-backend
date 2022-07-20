import unittest

from services.store_management.domain.usecases.get_revenue_by_day import GetRevenueByDayUsecase


class TestGetRevenueByDate(unittest.TestCase):
    def __init__(self):
        self.revenue_by_date = GetRevenueByDayUsecase()

    def test_get_revenue_in_today(self):
        total = self.revenue_by_date.execute()
        self.assertTrue(total > 1000000)

    def test_get_revenue_input_is_not_date(self):
        with self.assertRaises(TypeError):
            self.revenue_by_date.execute(start_date='test_date')


if __name__ == '__main__':
    unittest.main()
