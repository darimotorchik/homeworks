def create_odd_number_list(number):
    new_list = []
    for num in range(number + 1):
        if num % 2:
            new_list.append(num)
    print(f'Список из нечётных чисел от одного до {number}: {new_list}')


user_num = int(input('Введите число: '))
create_odd_number_list(user_num)