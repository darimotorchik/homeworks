def detect_the_language(user_string):
    alphabet_rus = tuple(list(chr(i) for i in range(ord('а'), ord('е') + 1)) + list('ё') + list(
        chr(i) for i in range(ord('ж'), ord('я') + 1)))
    alphabet_eng = tuple(chr(i) for i in range(ord('a'), ord('z') + 1))
    flag = 0

    for symbol in user_string:
        if not symbol.isalpha():
            continue
        elif (symbol.lower() in alphabet_rus) and (flag == 0 or flag == 1):
            flag = 1
            continue
        elif (symbol.lower() in alphabet_eng) and (flag == 0 or flag == 2):
            flag = 2
            continue
        else:
            print('Ошибка: используются неизвестные языки или в одном тексте используются разные языки')
            break
    else:
        if flag == 1:
            return alphabet_rus
        return alphabet_eng


def caesar_cipher(user_string, user_shift, alphabet):
    result = ''
    for symbol in user_string:
        flag_upper = False
        if symbol.isalpha():
            if symbol.isupper():
                flag_upper = True
            symbol_i = alphabet.index(symbol.lower())
            if symbol_i + user_shift > len(alphabet) - 1:
                if flag_upper:
                    result += alphabet[abs(len(alphabet) - symbol_i - user_shift)].upper()
                else:
                    result += alphabet[abs(len(alphabet) - symbol_i - user_shift)]
            else:
                if flag_upper:
                    result += alphabet[symbol_i + user_shift].upper()
                else:
                    result += alphabet[symbol_i + user_shift]
        else:
            result += symbol
    return result


text = input('Введите сообщение (на русском или английском языке, использовать два языка в одном сообщении нельзя): ')
shift = int(input('Введите сдвиг: '))
text_alphabet = detect_the_language(text)
print(f'Зашифрованное сообщение: {caesar_cipher(text, shift, text_alphabet)}')
