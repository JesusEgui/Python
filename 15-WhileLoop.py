goal_score = 100
current_score = 0

print('''
===================================
======= Basketball Game ==========
===================================
''')

while current_score < goal_score:
    points = int(input('How many points did you score in the last round? '))
    current_score += points
    print(f'Your current score is {current_score} points.')

print('Congratulations! You reached the goal score of 100 points.')
