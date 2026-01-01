import csv
import shutil
from typing import List, Optional
from .Writer import Writer
from .Question import Question

class QuizletWriter(Writer):
    skipAI = True
    def __init__(self, template_path:str = "QuizGameCreator/Writer/Templates/Quizlet.tsv") -> None:
        self.template_path = template_path
        self.questions: List[Question] = []
    
    def add_question(self, question: Question) -> None:
        self.questions.append(question)
    
    def add_questions(self, questions: List[Question]) -> None:
        self.questions.extend(questions)
    
    def _question_to_row(self, question: Question, question_number: int = -1) -> List[str]:
        return [question.question_text, question.answers[question.correct_answers[0]-1]]
    
    def write(self, output_path: str) -> None:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='\t')
            for question in self.questions:
                row = self._question_to_row(question)
                writer.writerow(row)
    
    def clear(self) -> bool:
        self.questions.clear()
        return True

if __name__ == "__main__":
    q1 = Question(
        question_text="What is 1+1?",
        answer1="2",
        answer2="3",
        answer3="4",
        answer4="5",
        time_limit=30,
        correct_answers=[1]
    )
    
    q2 = Question(
        question_text="What is the capital of France?",
        answer1="Berlin",
        answer2="London",
        answer3="Paris",
        answer4="Madrid",
        time_limit=30,
        correct_answers=[3]
    )
    
    q3 = Question(
        question_text="What is the, largest planet in our solar system?",
        answer1="Earth",
        answer2="Jupiter",
        answer3="Mars",
        answer4="Saturn",
        time_limit=30,
        correct_answers=[2]
    )
    
    writer = QuizletWriter()
    writer.add_question(q1)
    writer.add_question(q2)
    writer.add_question(q3)
    writer.write("quizlet_output.csv")
