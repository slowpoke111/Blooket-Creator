import random
from BlooketCreator import BlooketCreator
from AI_Client.HackclubAPI import HackclubAPI
import time

API = HackclubAPI()
writer:BlooketCreator = BlooketCreator("./output.csv",30,API)

questionTime: int = 30
output_file: str = "blooket_output.csv"

with open("questions.txt", encoding="UTF-8") as f:
    text: list[str] = f.readlines()
    lines: list[str] = [i.strip() for i in text]

isAns:bool = False
question: str = ""
answer:str = ""
for line in lines:
    if not isAns:
        question=line
    else:
        answer = line
        writer.add_question(question,answer)
        
        answer = ""
        question = ""
    isAns = not isAns
    time.sleep(1) # To avoid rate limiting
writer.write_to_file()
