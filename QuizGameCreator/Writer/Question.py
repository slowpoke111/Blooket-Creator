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
        correct_answers: Optional[List[int]] = None,
        maxTimeLimit: int = 300
    ):
        self.question_text = question_text
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3 or ""
        self.answer4 = answer4 or ""
        self.time_limit = min(time_limit, maxTimeLimit)  
        self.correct_answers = correct_answers or [1]