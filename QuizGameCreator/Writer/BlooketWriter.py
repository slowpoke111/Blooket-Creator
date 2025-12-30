import csv
import shutil
from typing import List, Optional
from .Writer import Writer
from .Question import Question

class BlooketWriter(Writer):
    skipAI = False
    def __init__(self, template_path: str = "Blooket\\Writer\\Templates\\Blooket.csv"):

        self.template_path = template_path
        self.questions: List[Question] = []
    
    def add_question(self, question: Question) -> None:
        self.questions.append(question)
    
    def add_questions(self, questions: List[Question]) -> None:
        self.questions.extend(questions)
    
    def _question_to_row(self, question: Question, question_number: int) -> List[str]:
        correct_str = ",".join(str(ans) for ans in question.correct_answers)
        
        row = [
            str(question_number),
            question.question_text,
            question.answer1,
            question.answer2,
            question.answer3,
            question.answer4,
            str(question.time_limit),
            correct_str
        ]
        
        row.extend([""] * (26 - len(row)))
        
        return row
    
    def write(self, output_path: str) -> None:
        shutil.copy(self.template_path, output_path)
        
        with open(output_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        for i, question in enumerate(self.questions):
            row_index = 2 + i  
            if row_index < len(rows):
                rows[row_index] = self._question_to_row(question, i + 1)
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    
    def clear(self) -> None:
        self.questions.clear()


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
        question_text="What is 12*12?",
        answer1="144",
        answer2="120",
        answer3="132",
        answer4="156",
        time_limit=30,
        correct_answers=[1]
    )
    
    q3 = Question(
        question_text="Is 3 prime or composite?",
        answer1="prime",
        answer2="composite",
        time_limit=30,
        correct_answers=[1]
    )
    
    writer = BlooketWriter()
    writer.add_questions([q1, q2, q3])
    
    writer.write("./data/output.csv")
    print("Questions written to output.csv")
