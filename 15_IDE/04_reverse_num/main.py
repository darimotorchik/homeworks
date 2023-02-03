def edit_reverse_number(num):
    number_list = num.split('.')
    reverse_number = []
    for number in number_list:
        reverse_number.append(str(number)[::-1])
    result = '.'.join(reverse_number)
    return result


num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
num_1_reverse = edit_reverse_number(str(num_1))
num_2_reverse = edit_reverse_number(str(num_2))
print(f'Первое число наоборот: {num_1_reverse}')
print(f'Второе число наоборот: {num_2_reverse}')
print(f'Сумма: {float(num_1_reverse) + float(num_2_reverse)}')