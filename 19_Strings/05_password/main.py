while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8:
        print('Попробуйте ещё раз.')
        continue

    big_letter = sum([sym.isupper() for sym in password])
    numbers = sum([sym.isdigit() for sym in password])

    if big_letter >= 1 and numbers >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Попробуйте ещё раз.')