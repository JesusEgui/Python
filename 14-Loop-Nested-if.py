answer_a = input('Do you like photography? y/n: ')
if answer_a == 'y':
    print('That\'s great!')
    answer_b = input('Do you own a DSLR camera? y/n: ')
    if answer_b == 'y':
        print('Awesome! You can capture some amazing shots.')
    else:
        print('No worries, you can still take great photos with your phone!')
else:
    print('No problem, photography is not for everyone!')
