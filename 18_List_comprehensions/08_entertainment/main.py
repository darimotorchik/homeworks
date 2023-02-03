import random

stick_num = int(input('Количество палок: '))
throw_num = int(input('Количество бросков: '))
duets_num = [sorted([random.randint(1, stick_num), random.randint(1, stick_num)]) for _ in range(throw_num)]
print(f'Пары чисел: {duets_num}')
result = ['I' for j in range(1, stick_num + 1)]
for i in range(throw_num):
    print(f'Бросок {i + 1}. Сбиты палки с номера {duets_num[i][0]} по номер {duets_num[i][1]}')
    for j in range(1, stick_num + 1):
        if duets_num[i][0] <= j <= duets_num[i][1]:
            result[j - 1] = '.'
print('\nРезультат: ', end='')
print(*result, sep='')
