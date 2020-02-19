from unittest import TestCase, expectedFailure, main
from unittest.mock import patch
from pathlib import Path

from ..spanish_dict_client import SpanishDictionaryClient, HTTPException

class SpanishDictionaryClientTests(TestCase):
    def setUp(self):
        self.get_patcher = patch('requests.get')
        self.addCleanup(self.get_patcher.stop)
        self.mock_get = self.get_patcher.start()
        self.mock_get.return_value.status_code = 200

        with open(Path(__file__).parent / 'sample_response.json') as file:
            self.mock_get.return_value.text = file.read()

        self.client = SpanishDictionaryClient('an_api_key')

    def test_get_spanish_short_definitions(self):
        result = self.client.get_spanish_short_definitions("butter")
        self.assertTrue("comida" in result)
        self.mock_get.assert_called_once()
    

    def test_get_spanish_short_definitions_throws_on_bad_request(self):
        self.mock_get.return_value.status_code = 400
        self.assertRaises(HTTPException, self.client.get_spanish_short_definitions, "butter")


if __name__ == '__main__':
    main()
