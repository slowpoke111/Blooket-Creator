from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
class AIClient(ABC):
    @abstractmethod
    def generate_distractors(self, question: str, correct_answer: str) -> List[Optional[str]]:
        pass
