# Jak zapewne wiesz, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1 – 49.
# Zadaniem gracza jest poprawne wytypowanie losowanych liczb. Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.
#
# Napisz program, który:
#
# zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
# czy wprowadzony ciąg znaków jest poprawną liczbą,
# czy użytkownik nie wpisał tej liczby już poprzednio,
# czy liczba należy do zakresu 1-49,
# po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
# wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
# poinformuje gracza, ile liczb trafił.

import random


def symulator_lotto():
    lotto_scope = [i for i in range(1, 50)]
    random.shuffle(lotto_scope)
    lotto_result = lotto_scope[:6]
    result = False
    counter = 0
    print('Try your luck and provide us six numbers in range 1-49.\nPlease use a whitespace as a separator:')
    while not result:
        ticket = input()
        ticket_list = ticket.split()
        if len(ticket_list) == 6:
            try:
                ticket_numbers = []
                for element in ticket_list:
                    check_element = int(element)
                    ticket_numbers.append(check_element)
                    if ticket_numbers.count(check_element) == 1:
                        if check_element in range(1, 50):
                            if check_element in lotto_result:
                                counter = counter + 1
                            else:
                                continue
                            result = True
                        else:
                            print('Some numbers provided are not in range 1-49. Try again!')
                            counter = 0
                            result = False
                            break
                    else:
                        print('Some numbers provided occures more than once. Try again!')
                        counter = 0
                        result = False
                        break
            except ValueError:
                print('Some elements provided are not numbers. Try again!')
                result = False
        elif len(ticket_list) < 6:
            print('Too less elements provided. Try again!')
            result = False
        else:
            print('Too many elements provided. Try again!')
            result = False
    print(f'Winning numbers are {lotto_result}. You hit {counter} of them.')


symulator_lotto()
