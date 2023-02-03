def my_sort(num_list):
    for _ in range(len(num_list) - 1):
        for i_el in range(len(num_list) - 1):
            if num_list[i_el] > num_list[i_el + 1]:
                num_list[i_el], num_list[i_el + 1] = num_list[i_el + 1], num_list[i_el]
    return num_list


class_1 = list(range(160, 177, 2))
class_2 = list(range(162, 181, 3))
print(f'Класс 1: {class_1}', f'Класс 2: {class_2}', sep='\n')
class_1.extend(class_2)
print(f'Отсортированный список учеников: {my_sort(class_1)}')
