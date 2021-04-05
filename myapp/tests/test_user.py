import unittest
from myapp.services import user
import pprint


class TestUser(unittest.TestCase):
    def test_user(self):
        NAME_TO_FIND = "ahlev"
        user.insert_user(NAME_TO_FIND)
        results = user.find_user(NAME_TO_FIND)
        assert results[0]["name"] == NAME_TO_FIND
