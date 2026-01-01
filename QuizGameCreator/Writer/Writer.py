from abc import ABC, abstractmethod
from typing import List
from .Question import Question
from .QuestionBank import QuestionBank
class Writer(ABC):
    skipAI: bool = False
    @abstractmethod
    def add_question(self, question:Question) -> None:
        pass

    @abstractmethod
    def add_questions(self, questions:List[Question]) -> None:
        pass
    
    def add_question_bank(self, question_bank:QuestionBank) -> None:
        for question in question_bank.get_all_questions():
            self.add_question(question)
    
    @abstractmethod
    def write(self, output_path:str) -> None:
        pass
    
    @abstractmethod
    def _question_to_row(self, question:Question, question_number:int) -> List[str]:
        pass
    
    @abstractmethod
    def clear(self) -> bool:
        pass