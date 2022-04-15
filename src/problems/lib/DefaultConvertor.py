from src.problems.lib.Convertor import Convertor


class DefaultConvertor(Convertor):
    @staticmethod
    def encode(decoded: any):
        return decoded

    @staticmethod
    def decode(encoded: any):
        return encoded
