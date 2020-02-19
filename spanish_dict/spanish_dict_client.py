import requests
import logging
import json
import time


API_ROOT_URL = "https://www.dictionaryapi.com/api/v3/references/spanish/json/"

class HTTPException(Exception):
    pass

class InvalidWord(ValueError):
    pass

class SpanishDictionaryClient:
    """
    A simple client to translate english words to spanish

    https://www.dictionaryapi.com/api/v3/references/spanish/json/language?key=your-api-key
    """

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.root_url = API_ROOT_URL
        self.logger = logging.getLogger(__name__)

    def get_spanish_short_definitions(self, english_word):

        if not english_word or len(english_word) > 100:
            raise InvalidWord

        self.logger.info(f"Requesting translation for '{english_word}'")


        url = self.root_url + english_word
        req_start = time.perf_counter()
        response = requests.get(url, params={ 'key': self.apiKey })
        req_end = time.perf_counter()
        self.logger.info(f'Fetched definition for {english_word} in {req_end - req_start:0.4f}s')
        
        if response.status_code == 200:
            result = json.loads(response.text)
            if len(result) > 0:
                defs = result[0]['shortdef']
                return [term.strip() for terms in defs for term in terms.split(',') ]
            
            if len(result) == 0:
                raise InvalidWord

        self.logger.error(f"{url} yielded a {response.status_code} status code")
        raise HTTPException(f"{url} yielded a {response.status_code} status code")



