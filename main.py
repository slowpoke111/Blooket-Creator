from QuizGameCreator.SetCreator import SetCreator
from QuizGameCreator.AI_Client.HackclubAPI import HackclubAPI
from QuizGameCreator.Writer.GimkitWriter import GimkitWriter
from QuizGameCreator.Writer.BlooketWriter import BlooketWriter
from QuizGameCreator.Writer.KahootWriter import KahootWriter
import time
from tqdm import tqdm

API = HackclubAPI()
WRITER = KahootWriter()
CREATOR:SetCreator = SetCreator(output_file="./data/output.xlsx", time_limit=30, writer=WRITER, api_client=API)

questionTime: int = 30

with open("./data/questions.txt", encoding="UTF-8") as f: #TODO: move to yaml
    text: list[str] = f.readlines()
    lines: list[str] = [i.strip() for i in text]

isAns:bool = False
question: str = ""
answer:str = ""
for line in tqdm(lines):
    if line == "": continue
    if not isAns:
        question=line
        isAns = True
    else:
        answer = line
        CREATOR.add_question(question,answer)
        print(f"Q: {question}\nA: {answer}\nGenerating distractors...\n\n")
        answer = ""
        question = ""
        isAns = False
CREATOR.write_to_file()

if isAns and question:
    print(f"Warning: last question has no answer and was skipped: {question}")
