import unittest
from datetime import datetime

from ..tasks import mail_send, check_date

class TestTask(unittest.TestCase):

    def test_date_range(self):
        old_date = datetime.strptime('15-08-2022', "%d-%m-%Y")
        new_date = datetime.strptime('20-08-2022', "%d-%m-%Y")
        date_range = (old_date, new_date)
        self.assertTrue(date_range)