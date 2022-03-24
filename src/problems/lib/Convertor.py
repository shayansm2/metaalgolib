from abc import ABC, abstractmethod

from src.lib.FunctionObject import FunctionObject


class Convertor(FunctionObject, ABC):
    @staticmethod
    @abstractmethod
    def decode(encoded: any):
        pass

    @staticmethod
    @abstractmethod
    def encode(decoded: any):
        pass
