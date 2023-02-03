def find_palindrome(word):
    len_of_slice = int((len(word) - len(word) % 2) / 2)
    word_list = list(word)

    first_half = word_list[:len_of_slice]
    end_of_slice = len_of_slice - (len(word) + 1) % 2
    second_half = word_list[:end_of_slice:-1]

    if first_half == second_half:
        result = 'Слово является палиндромом'
    else:
        result = 'Слово не является палиндромом'
    print(result)


user_word = input('Введите слово: ')
find_palindrome(user_word)