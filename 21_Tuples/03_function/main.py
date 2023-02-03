import random


def cut_by_element(some_tuple):
    some_element = input('Введите элемент: ')
    elem_count = some_tuple.count(some_element)
    if elem_count >= 2:
        return some_tuple[some_tuple.index(some_element):
                          some_tuple.index(some_element, some_tuple.index(some_element) + 1) + 1]
    elif elem_count == 1:
        return some_tuple[some_tuple.index(some_element):]
    return tuple()


user_tuple = tuple(str(random.randint(0, 100)) for _ in range(50))
print(user_tuple)
print(type(user_tuple))
print(cut_by_element(user_tuple))

