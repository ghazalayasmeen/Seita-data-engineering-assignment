import unittest
from fastapi.testclient import TestClient
from seita_api.main import app
from configs import now_datetime, then_datetime


class TestEndpoints(unittest.TestCase):
    """
    Test cases for the FastAPI endpoints in the Seita Energy Flexibility application.
    """

    def setUp(self):
        """
        Set up the test client before each test case.
        """
        self.tester = TestClient(app)

    def test_forecasts_endpoint(self):
        """
        Test the /forecasts endpoint to ensure it returns a 200 status code.
        """
        url = f"/forecasts?now={now_datetime.replace('+', '%2B')}&then={then_datetime.replace('+', '%2B')}"
        response = self.tester.get(url)
        if response.status_code != 200:
            print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)

    def test_tomorrow_endpoint(self):
        """
        Test the /tomorrow endpoint to ensure it returns a 200 status code.
        """
        url = f"/tomorrow?now={now_datetime.replace('+', '%2B')}"
        response = self.tester.get(url)
        if response.status_code != 200:
            print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
