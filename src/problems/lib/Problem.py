from abc import ABC, abstractmethod

import pandas as pd
import requests as requests

from src.lib.DataStructure import DataStructure
from src.problems.lib.ParameterStorage import ParameterStorage
from src.problems.lib.ProblemCalculator import ProblemCalculator


class Problem(DataStructure, ABC):
    def __init__(self):
        self.parameters = None

    @abstractmethod
    def get_problem_name(self) -> str:
        pass

    @abstractmethod
    def get_parameter_storage(self) -> ParameterStorage:
        pass

    @abstractmethod
    def get_problem_calculator(self) -> ProblemCalculator:
        pass

    @abstractmethod
    def get_problem_convertors_mapping(self) -> dict:
        pass

    @abstractmethod
    def get_problem_operators_mapping(self) -> dict:
        pass

    @abstractmethod
    def set_parameters(self, *args):
        self.parameters = self.get_parameter_storage()
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
