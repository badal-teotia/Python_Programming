# Making a quiz game.

questions = ('Who is strongest man? : ',
             'Which planet is hottest in solar system? :',
             'How many zeros in 1 crore? : ',
             'How many planet in solar system? :')

correct_answers = ('B','C','C','C')

answers = (('A. Badal','B. Hanuman','C. Jamvant'),
           ('A. Earth','B. Mars','C. Venus'),
           ('A. 6','B. 8','C. 7'),
           ('A. 10','B. 8','C. 9'))

question_no = 0
score = 0

for question in questions:
    print('-------------------------')
    print(question)
    
    for answer in answers[question_no]:
        print(answer)
        
    user = input('Give answer (A,B,C) : ').upper()
    
    if user == correct_answers[question_no]:
        score += 1
        print('----CORRECT----')
    else:
        print('!!!!--INCORRECT')
        print(f'The correct answer is {correct_answers[question_no]}')
        
    question_no += 1
    
print('###############')
print(f'You scored {score} out of {question_no}')
print('###############')
