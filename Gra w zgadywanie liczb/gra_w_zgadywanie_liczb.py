# Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
#
# Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
# Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!",
# po czym wrócić do pkt. 1
# Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "To small!",
# po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "To big!",
# po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!",
# po czym zakończyć działanie programu.

import random


def guess_the_number():
    random_num = random.randint(1, 101)
    result = False
    print('Guess the number in range 1-100:')
    while not result:
        guess = input()
        try:
            guess_num = int(guess)
            if guess_num == random_num:
                print('You win!')
                result = True
            elif guess_num > random_num:
                print('Too big! Keep trying!')
                result = False
            else:
                print('Too small! Keep trying!')
                result = False
        except ValueError:
            print('It is not a number. Please try again with a right value.')


guess_the_number()
