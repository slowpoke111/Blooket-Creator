from .AIClient import AIClient
from anthropic import Anthropic
import os
from dotenv import load_dotenv
from typing import List, Optional

class ClaudeAPI(AIClient):
    rateLimit: int = 20
    def __init__(self, model:str) -> None:
        load_dotenv("./.env")
        api_key: Optional[str] = os.getenv("CLAUDE_API_KEY")

        if not api_key:
            raise ValueError("CLAUDE_API_KEY not found in .env file")

        self.client: Anthropic = Anthropic(api_key=api_key)
        self.model = model
    
    def generate_distractors(self, question: str, correct_answer: str) -> List[Optional[str]]:
        prompt: str = f"""Given the following question and correct answer, generate exactly 3 plausible but incorrect answer choices (distractors).

        Question: {question}
        Correct Answer: {correct_answer}

        If this question doesn't make sense as a multiple choice question (e.g., it's open-ended, requires a long explanation, or is subjective), respond with only the word "INVALID".

        Otherwise, provide exactly 3 distractors, one per line, with no numbering or bullets. The distractors should be:
        - Plausible but clearly incorrect
        - Similar in length and format to the correct answer
        - Common misconceptions or reasonable alternatives

        Distractors:"""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=5000,
                temperature=0.4,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            content: Optional[str] = str(response.content[0].text) #type: ignore

            if content:
                content = content.strip()
            else:
                content = ""

            if "INVALID" in content.upper()[:20]:
                return []

            lines: List[str] = [line.strip() for line in content.split('\n') if line.strip()]

            distractors: List[Optional[str]] = [line for line in lines if line and not line.lower().startswith('distractor')]

            if len(distractors) >= 3:
                return distractors[:3]
            else:
                return distractors
        except Exception as e:
            print(f"Error generating distractors with ClaudeAPI: {e}")
            return []
   