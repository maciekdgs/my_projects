def guess_number():
    print('Think a number in range 0-1000 and I will try to guess it in at most 10 steps!\nAre you ready?')
    maximum = 1000
    minimum = 0
    counter = 0
    while True:
        guess = int((maximum - minimum) / 2 + minimum)
        print(f'I guess you think about {guess}... Am I right?')
        answer = input('1: You are right!\n2: Too small\n3: Too big\n')
        if answer == '1':
            print(f'I knew it! Thank you, it was a pleasure to play with you.\nIt took me {counter} tries to find the right number!')
            return True
        elif answer == '2':
            minimum = guess
            counter = counter + 1
        elif answer == '3':
            maximum = guess
            counter = counter + 1
        else:
            print('Please give me a hint as a number in range 1-3.')


guess_number()
