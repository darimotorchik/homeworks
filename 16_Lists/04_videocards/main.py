def edit_number_list(number):
    number_list = []
    for num in range(number):
        number_list.append(int(input(f'{num + 1} видеокарта: ')))
    return number_list


def delete_max_number(num_list):
    new_num_list = []
    for num in num_list:
        if num == max(num_list):
            continue
        new_num_list.append(num)
    return new_num_list


user_number = int(input('Количество видеокарт: '))
user_number_list = edit_number_list(user_number)
print(f'\nСтарый список видеокарт: {user_number_list}')
user_new_number_list = delete_max_number(user_number_list)
print(f'Новый список видеокарт: {user_new_number_list}')

