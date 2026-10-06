import unittest
from startxpy import main

class TestMain(unittest.TestCase):
    def test_import_ok(self):
        self.assertTrue(hasattr(main, "main"))

if __name__ == "__main__":
    unittest.main()
