from definicli import start_logger
import requests

from definicli.api.errors import NetworkError

LOG_NAME = 'api'

LOG = start_logger(LOG_NAME)

class WordsAPI:
    def __init__(self):
        self.log_name = LOG_NAME + '.WordsAPI'
        self.log = start_logger(self.log_name)

        self.log.debug(f"{self.log_name} initializing...")

        self.url = "https://wordsapiv1.p.rapidapi.com/words/"

        self.headers = {
            'x-rapidapi-key': "",
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    def authenticate(self, api_key):
        """
        
        Add API key to lookup headers 

        Parameters:
            api_key (str): Your API key for wordsapiv1.p.rapidapi.com

        """
        self.headers['x-rapidapi-key'] = api_key

    def get_lookup_segments(self, word:str):
        res = f"{word}/definitions"

        return res

    def get_response(self, word:str):
        """
        
        Lookup a given term on the WordsAPI

        Parameters:
            word (str): A word that you'd like the definition to.

        """
        lkup = self.get_lookup_segments(word)
        lkup_url = self.url + lkup

        res = requests.request("GET", lkup_url, headers=self.headers)

        if res.status_code == 200:
            return res.json()['definitions']
        else:
            raise NetworkError()


API = WordsAPI()


def lookup_word(word):
    """
    
    Using the WordsAPI API lookup the definition for given word.

    Parameters:
        word (str): The word to which you'd like the definition.

    """
    defs = API.get_response(word)

    return API.get_response(word)


def clean_response(word, response):
    lines = []
    for entry in response:
        definition = entry['definition']
        pos = entry['partOfSpeech']

        line = f"{word} | {pos} | - {definition}"

        lines.append(line)

    return lines


