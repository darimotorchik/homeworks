def find_number(weight_list, new_weight):
    counter = 1
    for weight in weight_list:
        if new_weight <= weight:
            counter += 1
    print(f'\nНомер, куда встанет новый контейнер: {counter}')


number_of_container = int(input('Кол-во контейнеров: '))
user_weight_list = []
for _ in range(number_of_container):
    user_weight = input('Введите вес контейнера: ')
    while (float(user_weight) > 200) or (float(user_weight) % 1 != 0):
        user_weight = input('Ошибка ввода!\nЧисло должно быть целым и не больше 200\nПопробуйте еще раз: ')
    user_weight_list.append(int(user_weight))

user_new_weight = input('\nВведите вес нового контейнера: ')
while (float(user_new_weight) > 200) or (float(user_new_weight) % 1 != 0):
    user_new_weight = input('Ошибка ввода!\nЧисло должно быть целым и не больше 200\nПопробуйте еще раз: ')

find_number(user_weight_list, int(user_new_weight))
