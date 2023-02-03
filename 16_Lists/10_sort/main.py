def sort_list(number_list):
    for elem_1 in range(1, len(number_list)):
        first_notsorted_elem = number_list[elem_1]
        elem_2 = elem_1
        while elem_2 >= 1 and number_list[elem_2 - 1] > first_notsorted_elem:
            number_list[elem_2] = number_list[elem_2 - 1]
            elem_2 -= 1
        number_list[elem_2] = first_notsorted_elem
    print(f'Отсортированный список: {number_list}')


user_list = list(map(int, input('Введите числа для сортировки через пробел: ').split(' ')))
print(f'Изначальный список: {user_list}')
sort_list(user_list)
