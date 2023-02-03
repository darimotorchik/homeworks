def my_zip(some_string, some_tuple):
    min_len = min(len(some_string), len(some_tuple))
    result = ((i_str, some_tuple[some_string.index(i_str)]) for i_str in some_string[:min_len])
    return result


user_string = input('Строка: ')
user_tuple = tuple(map(int, input('Числа через пробел: ').split()))
print('\nРезультат:')
user_result = my_zip(user_string, user_tuple)
print(user_result)
for i_res in user_result:
    print(i_res)
