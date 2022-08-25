import unittest

from ..apis.update_pickup_time import pickupDate


class TestUpdatePickupTime(unittest.TestCase):
    time = '9999-12-31 23:59:59'

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_pickup_time_is_not_datetime_type(self):
        pickupDate('1', '123')

    def test_can_not_found_order(self):
        pickupDate('2', self.time)
    
    def test_update_false(self):
        pickupDate('2', self.time)
    
    def test_update_success(self):
        pickupDate('2', self.time)


if __name__ == '__main__':
    unittest.main()