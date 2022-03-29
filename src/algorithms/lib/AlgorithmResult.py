from typing import Optional

from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.lib.DataStructure import DataStructure


class AlgorithmResult(DataStructure):
    def __init__(self):
        self.bestAnswer = None
        self.answerLogs = []

    def set_best_answer(self, best_answer: EncodedSolution):
        self.bestAnswer = best_answer
        return self

    def get_best_answer(self) -> Optional[EncodedSolution]:
        return self.bestAnswer

    def insert_answer_log(self, answer: EncodedSolution):
        self.answerLogs.append(answer)
        return self

    def get_answer_logs(self) -> Optional[list[EncodedSolution]]:
        return self.answerLogs
