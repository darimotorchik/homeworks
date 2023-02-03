user_object = 'О Дивный Новый мир!'


def is_prime(num):
    if num in (0, 1):
        return False
    for divider in range(2, num // 2 + 1):
        if num % divider == 0:
            return False
    return True


def prime_index_sym_find(object_iterable):
    return [value for index, value in enumerate(object_iterable) if is_prime(index)]


print(f'Результат: {is_prime(0)}')
print(f'Результат: {prime_index_sym_find(user_object)}')
print(f'Результат: {prime_index_sym_find(list(range(100)))}')
print(f'Результат: {prime_index_sym_find([100, 200, 300, "буква", 0, 2, "а"])}')
