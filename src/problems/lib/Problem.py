from abc import ABC

import requests as requests


class Problem(ABC):
    def __init__(self):
        pass

    @staticmethod
    def get_from_url(url):
        request = requests.get(url)
        return request.text
