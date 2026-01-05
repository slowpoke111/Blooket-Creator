import csv
import shutil
from typing import List, Optional
from .Writer import Writer
from .Question import Question

class GimkitWriter(Writer):
    skipAI = False
    outputFormat = "csv"
    def __init__(self, template_path: str = "QuizGameCreator/Writer/Templates/Gimkit.csv"):
        self.template_path = template_path
        self.questions: List[Question] = []
    
    def add_question(self, question: Question) -> None:
        self.questions.append(question)
    
    def add_questions(self, questions: List[Question]) -> None:
        self.questions.extend(questions)
    
    def _question_to_row(self, question: Question, question_number: int) -> List[str]:
        correct_answer = question.answer1
        
        incorrect_answers = []
        if question.answer2:
            incorrect_answers.append(question.answer2)
        if question.answer3:
            incorrect_answers.append(question.answer3)
        if question.answer4:
            incorrect_answers.append(question.answer4)
        
        row = [question.question_text, correct_answer]
        
        for i in range(3):
            if i < len(incorrect_answers):
                row.append(incorrect_answers[i])
            else:
                row.append("")
        
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
            else:
                rows.append(self._question_to_row(question, i + 1))
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    
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
    
    writer = GimkitWriter()
    writer.add_questions([q1, q2, q3])
    
    writer.write("./data/gimkit_output.csv")
    print("Questions written to gimkit_output.csv")
