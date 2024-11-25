import unittest
from cache import ResponseCache

class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = ResponseCache()

    def test_set_and_get(self):
        self.cache.set("test_key", "test_value")
        self.assertEqual(self.cache.get("test_key"), "test_value")

    def test_clear_cache(self):
        self.cache.set("test_key", "test_value")
        self.cache.clear()
        self.assertIsNone(self.cache.get("test_key"))

if __name__ == "__main__":
    unittest.main()
