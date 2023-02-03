def symbol_frequency(text):
    symbol_dict = dict()
    for symbol in text:
        if symbol.lower() in symbol_dict:
            symbol_dict[symbol.lower()] += 1
        else:
            symbol_dict[symbol.lower()] = 1
    return symbol_dict


def invert_the_dict(symbol_dict):
    inverted_dict = dict()
    for i_val in symbol_dict.values():
        symbol_list = []
        for i_sym in symbol_dict:
            if symbol_dict[i_sym] == i_val:
                symbol_list.append(i_sym)
        inverted_dict[i_val] = symbol_list
    return inverted_dict


user_text = input('Введите текст: ')
sym_dict = symbol_frequency(user_text)
inv_dict = invert_the_dict(sym_dict)

print('Оригинальный словарь частот:')
for sym in sorted(sym_dict.keys()):
    print(f'{sym} : {sym_dict[sym]}')

print('\nИнвертированный словарь частот:')
for num in inv_dict:
    print(f'{num} : {inv_dict[num]}')
