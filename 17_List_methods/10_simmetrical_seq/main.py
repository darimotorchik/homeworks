print('Введите последовательность чисел через пробел: ', end='')
user_list = list(map(int, input().split(' ')))
print('Последовательность: ', end='')
print(*user_list)
new_nums = []
nums_i = 0

while user_list != user_list[::-1]:
    new_nums.append(user_list[nums_i])
    user_list = user_list[nums_i + 1:]

new_nums.reverse()
print(f'Нужно приписать чисел: {len(new_nums)}')
print('Сами числа: ', end='')
print(*new_nums)
