list_1 = list(map(int, input('Введите элементы первого списка через пробел: ').split(' ')))
list_2 = list(map(int, input('Введите элементы второго списка через пробел: ').split(' ')))

print(f'Первый список: {list_1}')
print(f'Второй список: {list_2}')

list_1.extend(list_2)
for elem in list_1:
    while list_1.count(elem) > 1:
        list_1.remove(elem)

print(f'\nНовый первый список с уникальными элементами: {list_1}')
