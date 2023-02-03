def my_zip(*args):
    min_len = min(len(i_arg) for i_arg in args)
    result = tuple((tuple(enumerate(i_arg))[i_len][1]) for i_len in range(min_len) for i_arg in args)
    num_of_elements = len(args)
    final_result = (result[start:start + num_of_elements] for start in range(0, len(result), num_of_elements))
    return final_result

# some_tpl = (1, 2, 3, 4, 5, 6)
# some_dct = {'a_dict': 1, 'b_dict': 2, 'c_dict': 3}
# some_set = {'1_set', '2_set', '3_set', '4_set'}
# some_str = 'abcdefg'
# some_list = [11, 12, 13]
# user_final_result = my_zip(some_tpl, some_dct, some_set, some_str, some_list)
# print('Результат:')
# print(user_final_result)
# for i_res in user_final_result:
#    print(i_res)
