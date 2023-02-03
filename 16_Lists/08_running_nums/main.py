def shift_line(number_list, number):
    print(f'Изначальный список: {number_list}')
    new_list = number_list[-number:]
    new_list.extend(number_list[:-number])
    print(f'Сдвинутый список: {new_list}')


user_number = int(input('Сдвиг: '))
user_list = []
length_of_list = int(input('Длина списка: '))
for _ in range(length_of_list):
    user_list.append(int(input('Элемент списка: ')))

shift_line(user_list, user_number)