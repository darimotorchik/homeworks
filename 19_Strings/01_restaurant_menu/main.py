menu_input = input('Доступное меню: ')
menu_list = menu_input.split(';')
print(f'На данный момент в меню есть: {", ".join(menu_list)}')
