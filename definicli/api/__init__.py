import requests

from definicli import NetworkError

class WordsAPI(object):
    def __init__(self):
        self.url = "https://wordsapiv1.p.rapidapi.com/words/"

        self.headers = {
            'x-rapidapi-key': "",
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

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
            return res
        else:
            raise NetworkError()



