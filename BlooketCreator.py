from BlooketWriter import BlooketWriter, Question
from AI_Client.AIClient import AIClient

class BlooketCreator:
    def __init__(self, output_file: str, time_limit: int, api_client:AIClient) -> None:
        self.output_file = output_file
        self.time_limit = time_limit
        self.api_client = api_client
        self.writer: BlooketWriter = BlooketWriter()
        
    def add_question(self, question_text: str, correct_answer: str) -> None:
        distractors = self.api_client.generate_distractors(question_text, correct_answer)
        
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
        
        self.writer.add_question(q)
    
    def write_to_file(self) -> None:
        self.writer.write(self.output_file)
    