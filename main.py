import random
from Blooket import BlooketCreator, HackclubAPI
import time
from tqdm import tqdm

API = HackclubAPI()
writer:BlooketCreator = BlooketCreator("./data/output.csv",30,API)

questionTime: int = 30

with open("./data/questions.txt", encoding="UTF-8") as f:
    text: list[str] = f.readlines()
    lines: list[str] = [i.strip() for i in text]

isAns:bool = False
question: str = ""
answer:str = ""
for line in tqdm(lines[:2]):
    if line == "": continue
    if not isAns:
        question=line
    else:
        answer = line
        writer.add_question(question,answer)
        print(f"Q: {question}\nA: {answer}\nGenerating distractors...\n\n")
        answer = ""
        question = ""
    isAns = not isAns
    time.sleep(1) # To avoid rate limiting
writer.write_to_file()
