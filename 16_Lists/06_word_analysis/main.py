def count_unique_letters(word):
    letters_list = list(word)
    unique_letter_list = []
    repeat_list = []
    for letter in range(len(letters_list)):
        if (letters_list[letter] not in letters_list[letter + 1:]) and (letters_list[letter] not in repeat_list):
            unique_letter_list.append(letters_list[letter])
        else:
            repeat_list.append(letters_list[letter])
    print('Уникальные буквы в слове: ', end='')
    print(*unique_letter_list, sep=', ')
    print(f'Количество уникальных букв: {len(unique_letter_list)}')


user_word = input('Введите слово: ')
count_unique_letters(user_word)
