from abc import ABC, abstractmethod

import pandas as pd
import requests as requests

from src.problems.lib.ParameterStorage import ParameterStorage


class Problem(ABC):
    def __init__(self):
        self.parameter = ParameterStorage()

    @abstractmethod
    def get_problem_name(self) -> str:
        pass

    @staticmethod
    def get_from_url(url: str):
        request = requests.get(url)
        return request.text

    @staticmethod
    def get_from_excel(path: str, sheet_name='Sheet1') -> pd.DataFrame:
        return pd.read_excel(path, sheet_name)

    @staticmethod
    def get_from_csv(path: str) -> pd.DataFrame:
        return pd.read_csv(path)
