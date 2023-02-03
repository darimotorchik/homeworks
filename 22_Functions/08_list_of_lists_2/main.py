nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
result_list = []


def unpack_list(some_list, res_list):
    for i_elem in some_list:
        if isinstance(i_elem, list):
            unpack_list(i_elem, res_list)
        else:
            res_list.append(i_elem)
    return res_list


result = unpack_list(nice_list, result_list)
print(f'Ответ: {result}')
