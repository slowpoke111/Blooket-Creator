"""
Quiz Game Creator Package
"""

from typing import TYPE_CHECKING

__version__ = "0.1.0"
__author__ = "Ben Bell"

__all__ = [
    "SetCreator",
    "BlooketWriter",
    "Question",
    "AIClient",
    "HackclubAPI",
    "OpenAIAPI",
]

if TYPE_CHECKING:
    from .SetCreator import SetCreator as _SetCreator
    from .Writer.BlooketWriter import BlooketWriter as _BlooketWriter
    from .Writer.Question import Question as _Question
    from .AI_Client.AIClient import AIClient as _AIClient
    from .AI_Client.HackclubAPI import HackclubAPI as _HackclubAPI
    from .AI_Client.OpenAIAPI import OpenAIAPI as _OpenAIAPI


def __getattr__(name):
    if name == "SetCreator":
        from .SetCreator import SetCreator  
        return SetCreator
    if name == "BlooketWriter":
        from .Writer.BlooketWriter import BlooketWriter  
        return BlooketWriter
    if name == "Question":
        from .Writer.Question import Question  
        return Question
    if name == "AIClient":
        from .AI_Client.AIClient import AIClient  
        return AIClient
    if name == "HackclubAPI":
        from .AI_Client.HackclubAPI import HackclubAPI 
        return HackclubAPI
    if name == "OpenAIAPI":
        from .AI_Client.OpenAIAPI import OpenAIAPI
        return OpenAIAPI
    raise AttributeError(f"module 'Blooket' has no attribute {name!r}")