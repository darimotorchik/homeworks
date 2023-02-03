def key_word_find(key_word, structure, depth=None, count=1):
    if key_word in structure:
        return structure[key_word]
    for substructure in structure.values():
        if isinstance(substructure, dict):
            counter = count + 1
            if depth and counter >= depth:
                return None
            result = key_word_find(key_word, substructure, count=counter)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key_word = input('Введите искомый ключ: ')
answer = input('Хотите ввести максимальную глубину? Y/N: ').strip().upper()
if answer == 'Y':
    user_depth = int(input('Введите максимальную глубину: '))
    user_result = key_word_find(user_key_word, site, user_depth)
else:
    user_result = key_word_find(user_key_word, site)
if user_result:
    print(f'Значение ключа: {user_result}')
else:
    print('Ключ не найден')
