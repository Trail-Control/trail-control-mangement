import unittest
from api import routes

class TestTweetsPost(unittest.TestCase):

    bad_json = "{'KcTrailsStatus: []}"
    good_json = '{"KcTrailsStatus": []}'

    def setUp(self):
        routes.app.config['TESTING'] = True
        self.test_app = routes.app.test_client()
        self.url = "/api/v1/tweets/"

    def test_post_data_recieved(self):
        response = self.test_app.post(self.url, json=self.good_json)
        self.assertEqual(response.status_code, 201)

    def test_post_bad_data(self):
        response = self.test_app.post(self.url, json=self.bad_json)
        self.assertEqual(response.status_code, 400)

    def test_post_no_data_recieved(self):
        response = self.test_app.post(self.url)
        self.assertEqual(response.status_code, 400)


class TestTweetsGet(unittest.TestCase):
    def setUp(self):
        routes.app.config['TESTING'] = True
        self.test_app = routes.app.test_client()
        self.url = "/api/v1/tweets/"

    def test_get_tweets(self):
        response = self.test_app.get(self.url)
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
