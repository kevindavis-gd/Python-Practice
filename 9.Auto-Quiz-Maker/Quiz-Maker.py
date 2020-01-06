from pathlib import Path
import os
import shelve
import random

home = Path.home()
location = Path(r'Desktop\Python-Practice\9.Auto-Quiz-Maker\quiz')
os.chdir(home / location)

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#create 35 different quizzes
for quizNum in range(35):
    #create quiz file and number it
    quizFile = open('quiz{quizNum + 1}.txt', 'w')
    #create answers to the quiz file
    answerKeyFile = open('quiz_answers{quizNum + 1}.txt', 'w')
    #write these items to quizfile
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write('State Capitals Quiz (From {quizNum + 1})')
    quizFile.write('\n\n')


for quizNum in range(35):
    quizFile = open(f'quiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'quiz_answers{quizNum + 1}.txt', 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20)+ f'State Capitals Quiz (From {quizNum + 1})')
    quizFile.write('\n\n')

    states = list(capitals.keys())

    for questionNum in range(50):
        #store correct answer to question
        correctAnswer = capitals[states[questionNum]]
        #store all answers to all questions
        AllAnswers=list(capitals.values())
        #delete the correct answer from list of answers
        del AllAnswers[AllAnswers.index(correctAnswer)]
        #choose 3 random answers from All Answers
        WrongAnswerChoices = random.sample(AllAnswers, 3)
        #add the correct answer to the selection
        answerOptions = WrongAnswerChoices + [correctAnswer]
        #shuffle the answers
        random.shuffle(answerOptions)

        #write questions to paper
        quizFile.write(f'{questionNum + 1}. What is the capital of{states[questionNum]}?\n')
        #write different choices
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write("\n")
        #write answer to question in answer sheet
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]} \n")

    quizFile.close()
    answerKeyFile.close()
    #shuffle list before another quiz paper
    random.shuffle(states)
    
