import unittest 
from city_functions import get_formatted_name

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        formattedName = get_formatted_name("Denver", "United States");
        self.assertEqual(formattedName, "Denver United States")


unittest.main()
