user_str = input('Введите строку: ')
if len(user_str) % 2 == 0:
    user_set = set(user_str)
    result = False
    if len(user_set) == len(user_str) // 2:
        result = True
else:
    symbol_count_dict = dict()
    for sym in user_str:
        symbol_count_dict[sym] = symbol_count_dict.get(sym, 0) + 1
    values_nums = symbol_count_dict.values()
    counter = 0
    result = True
    for value in values_nums:
        if value % 2 != 0:
            counter += 1
    if counter > 1:
        result = False
print('Можно сделать палиндромом' if result else 'Нельзя сделать палиндромом')
