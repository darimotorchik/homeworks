user_string = input('Введите строку: ')
first_h_index = user_string.index('h')
last_h_index = user_string.rindex('h')
reverse_string = user_string[last_h_index - 1:first_h_index:-1]
print(f'Развёрнутая последовательность между первым и последним h: {reverse_string}')
