"""
Blooket Creator Package
"""

from .BlooketCreator import BlooketCreator
from .BlooketWriter import BlooketWriter, Question
from .AI_Client.AIClient import AIClient
from .AI_Client.HackclubAPI import HackclubAPI
from .AI_Client.OpenAIAPI import OpenAIAPI

__version__ = "1.0.0"
__author__ = "Your Name"

__all__ = [
    "BlooketCreator",
    "BlooketWriter", 
    "Question",
    "AIClient",
    "HackclubAPI",
    "OpenAIAPI"
]