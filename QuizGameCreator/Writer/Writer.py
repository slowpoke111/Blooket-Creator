from abc import ABC, abstractmethod
from typing import List
from .Question import Question

class Writer(ABC):
    @abstractmethod
    def add_question(self, question:Question):
        pass

    @abstractmethod
    def add_questions(self, questions:List[Question]):
        pass
    
    @abstractmethod
    def write(self, output_path:str):
        pass
    
    @abstractmethod
    def _question_to_row(self, question:Question, question_number:int) -> List[str]:
        pass
    
    @abstractmethod
    def clear(self):
        pass