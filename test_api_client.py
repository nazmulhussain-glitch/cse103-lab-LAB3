"""Unit tests for the API data-processing helper."""

import unittest

from api_client import summarize_users


class ApiClientTests(unittest.TestCase):
    """Check that user records are converted into concise summaries."""

    def test_summarize_users_extracts_expected_fields(self):
        users = [{
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "sincere@example.com",
            "address": {"city": "Gwenborough"},
        }]

        result = summarize_users(users)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["name"], "Leanne Graham")
        self.assertEqual(result[0]["username"], "Bret")
        self.assertEqual(result[0]["email"], "sincere@example.com")
        self.assertEqual(result[0]["city"], "Gwenborough")

    def test_summarize_users_handles_missing_address(self):
        users = [{"id": 2, "name": "Ervin Howell"}]

        result = summarize_users(users)

        self.assertEqual(result[0]["id"], 2)
        self.assertIsNone(result[0]["city"])

    def test_summarize_users_handles_empty_input(self):
        self.assertEqual(summarize_users([]), [])


if __name__ == "__main__":
    unittest.main()
