first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')
max_shift = len(first_string) - 1
if first_string == second_string:
    print('Две строки равны!')
else:
    for shift in range(1, max_shift + 1):
        shift_string = ''.join([first_string[-shift:], first_string[:-shift]])
        if second_string == shift_string:
            print(f'Первая строка получается из второй со сдвигом {shift}')
            break
    else:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
