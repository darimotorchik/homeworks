def my_sort(num_list):
    for _ in range(len(num_list) - 1):
        for i_el in range(len(num_list) - 1):
            if num_list[i_el] > num_list[i_el + 1]:
                num_list[i_el], num_list[i_el + 1] = num_list[i_el + 1], num_list[i_el]
    return num_list


print('Введите список размеров коньков в конторе через пробел: ', end='')
skate_list = list(map(int, input().split(' ')))
print('\nВведите список размеров ног людей через пробел: ', end='')
human_list = list(map(int, input().split(' ')))

my_sort(skate_list)
my_sort(human_list)
counter = 0

while skate_list and human_list:
    if human_list[0] <= skate_list[0]:
        counter += 1
        human_list.remove(human_list[0])
        skate_list.remove(skate_list[0])
    else:
        skate_list.remove(skate_list[0])


print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {counter}')
