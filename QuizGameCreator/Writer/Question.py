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
        maxTimeLimit: int = 300,
        #Unused parameters 
        difficulty: Optional[int] = None,
        category: Optional[str] = None,
        tags: Optional[List[str]] = None,
        source: Optional[str] = None,
        explanation: Optional[str] = None,
    ):
        self.question_text = question_text
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3 or ""
        self.answer4 = answer4 or ""
        self.answers = [self.answer1, self.answer2, self.answer3, self.answer4]
        self.time_limit = min(time_limit, maxTimeLimit)  
        self.correct_answers = correct_answers or [1]
        # Unused attributes
        self.difficulty = difficulty
        self.category = category
        self.tags = tags or []
        self.source = source
        self.explanation = explanation
    
    def __repr__(self) -> str:
        return f"Question(question_text={self.question_text}, answers={self.answers}, time_limit={self.time_limit}, correct_answers={self.correct_answers}, difficulty={self.difficulty}, category={self.category}, tags={self.tags}, source={self.source}, explanation={self.explanation})"
    
    def __str__(self) -> str:
        return f"Q: {self.question_text}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}\nTime Limit: {self.time_limit}s\nCorrect Answers: {self.correct_answers}"
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Question):
            return False
        return (
            self.question_text == value.question_text and
            self.answers == value.answers and
            self.time_limit == value.time_limit and
            self.correct_answers == value.correct_answers and
            self.difficulty == value.difficulty and
            self.category == value.category and
            self.tags == value.tags and
            self.source == value.source and
            self.explanation == value.explanation
        )
        
    def to_dict(self) -> dict:
        return {
            "question_text": self.question_text,
            "answers": self.answers,
            "time_limit": self.time_limit,
            "correct_answers": self.correct_answers,
            "difficulty": self.difficulty,
            "category": self.category,
            "tags": self.tags,
            "source": self.source,
            "explanation": self.explanation
        }
    
    def __hash__(self) -> int:
        return hash((
            self.question_text,
            tuple(self.answers),
            self.time_limit,
            tuple(self.correct_answers),
            self.difficulty,
            self.category,
            tuple(self.tags),
            self.source,
            self.explanation
        ))
    
    def __bool__(self) -> bool:
        return bool(self.question_text and self.answer1 and self.answer2 and self.correct_answers)
