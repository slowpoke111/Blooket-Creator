from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
class AIClient(ABC):
    rateLimit:int = -1 #Per minute
    @abstractmethod
    def generate_distractors(self, question: str, correct_answer: str) -> List[Optional[str]]:
        pass
    
    def get_rate_limit(self) -> int:
        return self.rateLimit
