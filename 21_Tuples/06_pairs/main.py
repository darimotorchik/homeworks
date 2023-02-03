import random

# первый вариант решения
origin_list = [random.randint(0, 20) for _ in range(10)]
list1 = [value for index, value in enumerate(origin_list) if index % 2 == 0]
list2 = [value for index, value in enumerate(origin_list) if index % 2 != 0]
result = list(zip(list1, list2))
print(f'Оригинальный список: {origin_list}')
print(f'Новый список: {result}')


# второй вариант решения
origin_list = [random.randint(0, 20) for _ in range(10)]
print(f'Оригинальный список: {origin_list}')
result = []
for i_value in range(0, len(origin_list), 2):
    result.append((origin_list[i_value], origin_list[i_value + 1]))
print(f'Новый список: {result}')
