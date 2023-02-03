import random

max_num = int(input('Введите максимальное число: '))
guess_num = random.randint(1, max_num)
possibly_nums = set()
no_nums = set()

while True:
    answer = False
    estimated_nums = input('Нужное число есть среди вот этих чисел: ')
    if estimated_nums.title().strip() != 'Помогите!':
        estimated_nums_set = set(map(int, estimated_nums.split()))
        if guess_num in estimated_nums_set:
            answer = True
            if len(possibly_nums) == 0:
                possibly_nums.update(estimated_nums_set)
            else:
                possibly_nums = possibly_nums.intersection(estimated_nums_set)
        else:
            no_nums.update(estimated_nums_set)
        print('Ответ Артёма: Да' if answer else 'Ответ Артёма: Нет')
    elif estimated_nums.title().strip() == 'Помогите!' and len(possibly_nums) == 0:
        print('Попробуйте угадать хотя бы раз!')
        continue
    else:
        possibly_nums = possibly_nums - no_nums
        print('Артём мог загадать следующие числа: ', end='')
        print(*possibly_nums)
        break
    if len(estimated_nums_set) == 1 and answer:
        print('Вы угадали!')
        break
