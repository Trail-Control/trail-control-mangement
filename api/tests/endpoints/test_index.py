import unittest

from api import routes

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testC = routes.app.test_client()

    def test_index(self):
        response = self.testC.get('/')
        self.assertIsNotNone(response)
        code = response.status_code
        self.assertEqual(code, 200)


if __name__ == '__main__':
    unittest.main()
