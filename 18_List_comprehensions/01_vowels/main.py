vowels = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
user_text = [x for x in list(input('Введите текст: ')) if x in vowels]
print(f'Список гласных букв: {user_text}', f'Длина списка: {len(user_text)}', sep='\n')
