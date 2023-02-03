basic_list = [1, 5, 3]
secondary_1 = [1, 5, 1, 5]
secondary_2 = [1, 3, 1, 5, 3, 3]

basic_list.extend(secondary_1)
print(f'Кол-во цифр 5 при первом объединении: {basic_list.count(5)}')

while 5 in basic_list:
    basic_list.remove(5)

basic_list.extend(secondary_2)
print(f'Кол-во цифр 3 при втором объединении: {basic_list.count(3)}')
print(f'Итоговый список: {basic_list}')
