#! /usr/bin/env python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama':        'Montgomery',
            'Alaska':         'Juneau',
            'Arizona':        'Phoenix',
            'Arkansas':       'Little Rock',
            'California':     'Sacramento',
            'Colorado':       'Denver',
            'Connecticut':    'Hartford',
            'Delaware':       'Dover',
            'Florida':        'Tallahassee',
            'Georgia':        'Atlanta',
            'Hawaii':         'Honolulu',
            'Idaho':          'Boise',
            'Illinois':       'Springfield',
            'Indiana':        'Indianapolis',
            'Iowa':           'Des Moines',
            'Kansas':         'Topeka',
            'Kentucky':       'Frankfort',
            'Louisiana':      'Baton Rouge',
            'Maine':          'Augusta',
            'Maryland':       'Annapolis',
            'Massachusetts':  'Boston',
            'Michigan':       'Lansing',
            'Minnesota':      'Saint Paul',
            'Mississippi':    'Jackson',
            'Missouri':       'Jefferson City',
            'Montana':        'Helena',
            'Nebraska':       'Lincoln',
            'Nevada':         'Carson City',
            'New Hampshire':  'Concord',
            'New Jersey':     'Trenton',
            'New Mexico':     'Santa Fe',
            'New York':       'Albany',
            'North Carolina': 'Raleigh',
            'North Dakota':   'Bismarck',
            'Ohio':           'Columbus',
            'Oklahoma':       'Oklahoma City',
            'Oregon':         'Salem',
            'Pennsylvania':   'Harrisburg',
            'Rhode Island':   'Providence',
            'South Carolina': 'Columbia',
            'South Dakota':   'Pierre',
            'Tennessee':      'Nashville',
            'Texas':          'Austin',
            'Utah':           'Salt Lake City',
            'Vermont':        'Montpelier',
            'Virginia':       'Richmond',
            'Washington':     'Olympia',
            'West Virginia':  'Charleston',
            'Wisconsin':      'Madison',
            'Wyoming':        'Cheyenne'
            }

# generates 35 quiz/answer key files (can be altered to any number)
for x in range(35):
    quiz = open(f'quizzes/capitals_quiz{x + 1}.txt', 'w')
    answer_key = open(f'quizzes/capitals_quiz_answers{x + 1}.txt', 'w')
    quiz.write('Name:\n\nDate:\n\nPeriod\n\n')
    quiz.write((' ' * 20) + f'State Capitals Quiz (Form {x + 1})\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    # iterates over each state
    for Q in range(50):
        correct_answer = capitals[states[Q]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(capitals[states[Q]])
        answer_options = random.sample(wrong_answers, 3)
        answer_options += [correct_answer]
        random.shuffle(answer_options)

        quiz.write(f'{Q + 1}. What\'s the capital of {states[Q]}?\n')
        # creates 4 possible choices
        for i in range(4):
            quiz.write(f'\t{"ABCD"[i]}.\t{answer_options[i]}\n')
        quiz.write('\n')

        answer_key.write(f'{Q + 1}.\t{"ABCD"[answer_options.index(correct_answer)]}\n')

    quiz.close()
    answer_key.close()
