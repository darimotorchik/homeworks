user_string = input('Введите строку: ')
code_list = []
sym1_i = 0
sym2_i = 1
flag = False
while sym1_i < len(user_string) and sym2_i < len(user_string):
    while user_string[sym1_i] == user_string[sym2_i]:
        if sym2_i == len(user_string) - 1:
            sym2_i += 1
            break
        sym2_i += 1
    repeats = user_string[sym1_i:sym2_i].count(user_string[sym1_i])
    code_list.extend([user_string[sym1_i], str(repeats)])
    sym1_i = sym2_i
    sym2_i += 1
else:
    if user_string[-1] != user_string[-2]:
        code_list.extend([user_string[sym1_i], '1'])

code_string = ''.join(code_list)
print(f'Закодированная строка: {code_string}')
