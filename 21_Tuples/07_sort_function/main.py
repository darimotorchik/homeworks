def sort_the_tuple(origin_tuple):
    int_tuple = tuple(map(int, origin_tuple))
    if origin_tuple != int_tuple:
        print('Во введенных данных присутствует не целое число!')
        return ()
    some_list = list(int_tuple)
    len_tuple = len(int_tuple)
    for i in range(len_tuple - 1):
        for j in range(len_tuple - (i + 1)):
            if some_list[j] > some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
    some_tuple = tuple(some_list)
    return some_tuple


user_tuple = tuple(map(float, input('Введите элементы кортежа через пробел: ').split()))

print(f'Отсортированный по возрастанию кортеж: {sort_the_tuple(user_tuple)}')

