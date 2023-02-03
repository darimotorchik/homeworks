def move(n, x, y):
    if n == 1:
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
    else:
        tmp = 6 - x - y
        move(n - 1, x, tmp)
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        move(n - 1, tmp, y)


user_n = int(input('Введите количество дисков: '))
user_x = int(input('Введите исходный стержень: '))
user_y = int(input('Введите целевой стержень: '))

move(user_n, user_x, user_y)

