from .Writer.Question import Question
from .Writer.Writer import Writer
from .AI_Client.AIClient import AIClient
import time
from .Writer.QuestionBank import QuestionBank
class SetCreator:
    def __init__(self, output_file: str, time_limit: int, writer: Writer, api_client:AIClient) -> None:
        self.output_file = output_file
        self.time_limit = time_limit
        self.api_client = api_client
        self.writer: Writer = writer
        self.bank = QuestionBank()
        
    def add_question(self, question_text: str, correct_answer: str, skipAI: bool = False) -> None:
        
        if skipAI or self.writer.skipAI:
            q: Question = Question(
                question_text=question_text,
                answer1=correct_answer,
                answer2="",
                answer3="",
                answer4="",
                time_limit=self.time_limit,
                correct_answers=[1]
            )
            self.bank.add_question(q)
            return
        
        distractors = self.api_client.generate_distractors(question_text, correct_answer)

        if not distractors or all(not d for d in distractors):
            print(f"Warning: no distractors generated for question: {question_text}")
        
        while len(distractors) < 3:
            distractors.append("")
        
        q: Question = Question(
            question_text=question_text,
            answer1=correct_answer,
            answer2=distractors[0] or "",
            answer3=distractors[1] or "",
            answer4=distractors[2] or "",
            time_limit=self.time_limit,
            correct_answers=[1]
        )
        
        self.bank.add_question(q)

        if not skipAI and not self.writer.skipAI:
            rate_limit = self.api_client.get_rate_limit()
            if rate_limit > 0:
                time.sleep(60 / rate_limit)
    
    def write_to_file(self) -> None:
        self.writer.add_question_bank(self.bank)
        self.writer.write(self.output_file)
        self.writer.clear()
        
    def clear_questions(self) -> None:
        self.bank.clear()
        self.writer.clear()
    
    def load_questions_from_file(self, file_path: str) -> None:
        self.bank.load_from_file(file_path)
    
    def __len__(self) -> int:
        return self.bank.get_question_count()
    