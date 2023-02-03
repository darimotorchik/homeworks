def find_three_identical_numbers(num1, num2):
    digits_set = set()
    years_list = []
    digits_list = []
    for num in range(num1, num2 + 1):
        year = num
        digits_sum = 0
        while num != 0:
            digits_set.add(num % 10)
            digits_sum += num % 10
            num //= 10
        if len(digits_set) == 2 and ((digits_sum == max(digits_set) * 3 + min(digits_set)) or (
                digits_sum == min(digits_set) * 3 + max(digits_set))):
            years_list.append(year)
        digits_set.clear()
    return years_list


year_1 = int(input('Введите первый год: '))
year_2 = int(input('Введите второй год: '))
print(f'\nГода от {year_1} до {year_2} с тремя одинаковыми цифрами:')
print(*find_three_identical_numbers(year_1, year_2), sep='\n')
