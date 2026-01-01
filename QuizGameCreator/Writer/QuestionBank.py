from typing import List
from .Question import Question

class QuestionBank:
    def __init__(self) -> None:
        self.questions: List[Question] = []
    
    def add_question(self, question: Question) -> None:
        self.questions.append(question)
    
    def add_questions(self, questions: List[Question]) -> None:
        self.questions.extend(questions)
    
    def clear(self) -> None:
        self.questions = []
    
    def get_all_questions(self) -> List[Question]:
        return self.questions