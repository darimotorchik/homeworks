user_string = input('Сообщение: ')
sym_list = []
new_list = []
for sym in user_string:
    if sym.isalpha():
        sym_list.append(sym)
    else:
        new_list.extend(sym_list[::-1])
        sym_list = []
        new_list.append(sym)
result_string = ''.join(new_list)
print(result_string)
