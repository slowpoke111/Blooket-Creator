#Imports
import gspread
import random

sa=gspread.service_account(filename="service_account.json")#Change filename to json file for service account
sh=sa.open("Blooket Spreadsheet Import Template Testing")#Change to name of google sheet to edit(the google sheet must be shared with the service account)

wks=sh.worksheet("Sheet1")#Sets the sheet to edit

with open("questions.txt",encoding="UTF-8") as f:#Read in questions.txt
    text=f.readlines()
    lines=[i.strip() for i in text]#Create a list of questions and answers and remove newline characters

#Do not edit lines 14-19
questionsCount=0#Counts the number of questions
questions=[]#List of questions in order
answerOrder=[]#Stores the answer in order
lineNumber=3#Line number to start on
questiontime=[]#Stores the time for the question
answerNum=[]#Stores the answer number

answers={"False","True"} #fill with at least one string which can be an answer
time=30#the amount of time in seconds to give for each question(max 300)

#Lines 25-27 store incorrect answers (Do not edit)
answerList1=[]
answerList2=[]
answerList3=[]
#Tracks if the line is a question or an answer
flag=False

for item in lines: #Iterate through every item in lines
    if not flag:#If it is not an answer
        for char in item:#Iterates through each character to check for a "?"
            if char=="?":#Checks if it is a question or a empty line
                pos="B"+str(lineNumber)#The position of the edit
                questions.append([item])#Adds the edit to a list of edits to be made
                lineNumber+=1#Increases the line number
                questionsCount+=1#Increases the question count
                flag=not flag#Set the flag to True, meaning that the next line is the answer
    else:#If it is an answer
        answerOrder.append([item])#add the answer to the list of edits to be made
        answers.add(item)#add to the set of answers which are used to generate the incorrect answers to questions
        flag=not flag#Set the flag to False, the next line will be a question or a blank space

for i in range(questionsCount):#Set the time and answer number for each line
    questiontime.append([time])
    answerNum.append([1])

answers=list(answers)#Converts the set of answers to a list so it can be indexed
for i in range(questionsCount):
    #Line 48 adds random answers to the question
    answerList1.append([random.choice(answers)]);answerList2.append([random.choice(answers)]);answerList3.append([random.choice(answers)])

#Update the google sheet using the list of answers
wks.update("B3:B284", questions)
wks.update("C3:C284", answerOrder)
wks.update("D3:D284", answerList1);wks.update("E3:E284", answerList2);wks.update("F3:F284", answerList3)
wks.update("G3:G284",questiontime)
wks.update("H3:H284",answerNum)