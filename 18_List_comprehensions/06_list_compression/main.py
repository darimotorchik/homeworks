import random

list_number = int(input('Количество чисел в списке: '))
list_generate = [random.randint(0, 2) for _ in range(list_number)]
print(f'Список до сжатия: {list_generate}')
list_generate = [x for x in list_generate if x != 0]
print(f'Список после сжатия: {list_generate}')
