import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Optional
from .AIClient import AIClient

class HackclubAPI(AIClient):
    rateLimit:int = 5
    def __init__(self) -> None:
        load_dotenv('./.env')
        api_key: Optional[str] = os.getenv('HACKCLUB_API_KEY')
        
        if not api_key:
            raise ValueError("HACKCLUB_API_KEY not found in .env file")
        
        self.client: OpenAI = OpenAI(
            api_key=api_key,
            base_url="https://ai.hackclub.com/proxy/v1"
        )
    
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
            response = self.client.chat.completions.create(
                model="qwen/qwen3-32b",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=5000,
                extra_body={"reasoning_effort": "none"}  
            )
            
            content: Optional[str] = response.choices[0].message.content
            
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
            elif len(distractors) > 0:
                return distractors + [None] * (3 - len(distractors))
            else:
                return []
                
        except Exception as e:
            print(f"Error generating distractors: {e}")
            return [None, None, None]


if __name__ == "__main__":
    generator: HackclubAPI = HackclubAPI()
    
    question: str = "Who wrote Les Misérables?"
    answer: str = "Victor Hugo"
    distractors: List[Optional[str]] = generator.generate_distractors(question, answer)
    
    if not distractors:
        print("Question is not suitable for multiple choice")
    else:
        print(f"Question: {question}")
        print(f"Correct Answer: {answer}")
        print(f"Distractors: {distractors}")

