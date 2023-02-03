def fibonacci_series(num_pos):
    if num_pos in (1, 2):
        return 1
    return fibonacci_series(num_pos - 1) + fibonacci_series(num_pos - 2)


assert fibonacci_series(10) == 55, 'Неверные значения, ошибка в коде'
assert fibonacci_series(6) == 8, 'Неверные значения, ошибка в коде'

user_num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
user_result = fibonacci_series(user_num_pos)
print(f'Число: {user_result}')
