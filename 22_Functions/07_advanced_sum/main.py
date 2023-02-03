def my_sum(*obj):
    str_obj = str(obj)
    del_sym_obj = str_obj.translate({ord(i_sym): None for i_sym in '[],(){}'})
    new_list = list(map(int, del_sym_obj.split()))
    return sum(new_list)


"""print(my_sum([[1, 2, [3]], [1], 3]))
print(my_sum((1, 2, 3, 4, 5)))
print(my_sum({1, 2, 3}))
print(my_sum(1, 2, 3, 4, 5))"""
