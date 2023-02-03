def find_smallest_divisor(num):
    smallest_divisor = 0
    for number in range(2, num // 2 + 1):
        if num % number == 0:
            smallest_divisor = number
            break
    else:
        smallest_divisor = num
    return smallest_divisor


user_number = int(input('Введите число (n>1): '))
while user_number <= 1:
    user_number = int(input('Ошибка ввода! Число должно быть больше единицы.\nПопробуйте еще раз: '))
result = find_smallest_divisor(user_number)
print(f'Наименьший делитель, отличный от единицы: {result}')