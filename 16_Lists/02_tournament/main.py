def create_even_index_name_list(name_list):
    new_list = []
    for num in range(len(name_list)):
        if not(num % 2):
            new_list.append(name_list[num])
    print(f'Список участников: {name_list}')
    print(f'Первый день: {new_list}')


name_count = int(input('Сколько имен будем вводить: '))
user_name_list = []
for name in range(name_count):
    user_name_list.append(input(f'Ввведите {name + 1} имя: '))
create_even_index_name_list(user_name_list)
