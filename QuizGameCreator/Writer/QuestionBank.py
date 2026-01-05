from typing import List
from .Question import Question

class QuestionBank:
    def __init__(self) -> None:
        self.questions: List[Question] = []
    
    def __len__(self) -> int:
        return len(self.questions)
    
    def add_question(self, question: Question) -> None:
        self.questions.append(question)
    
    def add_questions(self, questions: List[Question]) -> None:
        self.questions.extend(questions)
    
    def clear(self) -> None:
        self.questions = []
    
    def get_all_questions(self) -> List[Question]:
        return self.questions
    
    def get_question_count(self) -> int:
        return self.__len__()
    
    def is_empty(self) -> bool:
        return self.__len__() == 0
    
    def save_to_file(self, file_path: str) -> None:
        with open(file_path, 'w', encoding='utf-8') as f:
            for question in self.questions:
                f.write(f"{question.question_text}\n")
                f.write(f"1. {question.answer1}\n")
                if question.answer2:
                    f.write(f"2. {question.answer2}\n")
                if question.answer3:
                    f.write(f"3. {question.answer3}\n")
                if question.answer4:
                    f.write(f"4. {question.answer4}\n")
                f.write("\n")
    
    def load_from_file(self, file_path: str) -> None:
        self.clear()
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            question_text = lines[i].strip()
            answer1 = lines[i + 1].strip()[3:]
            answer2 = lines[i + 2].strip()[3:] if i + 2 < len(lines) and lines[i + 2].startswith("2. ") else None
            answer3 = lines[i + 3].strip()[3:] if i + 3 < len(lines) and lines[i + 3].startswith("3. ") else None
            answer4 = lines[i + 4].strip()[3:] if i + 4 < len(lines) and lines[i + 4].startswith("4. ") else None
            
            question = Question(
                question_text=question_text,
                answer1=answer1,
                answer2=answer2,#type: ignore
                answer3=answer3,
                answer4=answer4
            )
            self.add_question(question)
            
            i += 5
            while i < len(lines) and lines[i].strip() == "":
                i += 1