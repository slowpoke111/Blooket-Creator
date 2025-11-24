import csv
import shutil
from typing import List, Optional


class Question:    
    def __init__(
        self,
        question_text: str,
        answer1: str,
        answer2: str,
        answer3: Optional[str] = None,
        answer4: Optional[str] = None,
        time_limit: int = 30,
        correct_answers: Optional[List[int]] = None
    ):
        self.question_text = question_text
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3 or ""
        self.answer4 = answer4 or ""
        self.time_limit = min(time_limit, 300)  
        self.correct_answers = correct_answers or [1]
    
    def to_row(self, question_number: int) -> List[str]:

        correct_str = ",".join(str(ans) for ans in self.correct_answers)
        
        row = [
            str(question_number),
            self.question_text,
            self.answer1,
            self.answer2,
            self.answer3,
            self.answer4,
            str(self.time_limit),
            correct_str
        ]
        
        row.extend([""] * (26 - len(row)))
        
        return row


class BlooketWriter:
    
    def __init__(self, template_path: str = "template.csv"):

        self.template_path = template_path
        self.questions: List[Question] = []
    
    def add_question(self, question: Question) -> None:
        self.questions.append(question)
    
    def add_questions(self, questions: List[Question]) -> None:
        self.questions.extend(questions)
    
    def write(self, output_path: str) -> None:
        shutil.copy(self.template_path, output_path)
        
        with open(output_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        for i, question in enumerate(self.questions):
            row_index = 2 + i  
            if row_index < len(rows):
                rows[row_index] = question.to_row(i + 1)
        
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
    
    # Create writer and add questions
    writer = BlooketWriter()
    writer.add_questions([q1, q2, q3])
    
    # Write to output file
    writer.write("output.csv")
    print("Questions written to output.csv")
