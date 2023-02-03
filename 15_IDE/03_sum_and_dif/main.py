def find_the_sum_of_digits(number):
    summ = 0
    while number != 0:
        summ += number % 10
        number //= 10
    return summ


def find_the_number_of_digits(number):
    result = 0
    while number != 0:
        result += 1
        number //= 10
    return result


num = int(input('Введите целое положительное число: '))
while num <= 0:
    num = int(input('Некорректное значение! Число должно быть положительным. Попробуйте еще раз\n'))
sum_of_digits = find_the_sum_of_digits(num)
number_of_digits = find_the_number_of_digits(num)
difference = sum_of_digits - number_of_digits
print(f'Сумма цифр: {sum_of_digits}', f'Кол-во цифр в числе: {number_of_digits}',
      f'Разность суммы и кол-ва цифр: {difference}', sep='\n')
