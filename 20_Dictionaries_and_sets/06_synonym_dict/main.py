def create_synonym_dict(number):
    synonym_dict = dict()
    for num in range(1, number + 1):
        list_pair = input(f'{num} пара: ').title().split(' - ')
        synonym_dict[list_pair[0]] = (f'Синоним: {list_pair[1]}', 0)
        synonym_dict[list_pair[1]] = (f'Синоним: {list_pair[0]}', 0)
    return synonym_dict


def find_synonym(synonym_dict):
    user_word = input('\nВведите слово: ').capitalize()
    result = synonym_dict.get(user_word, ('Такого слова в словаре нет.', 1))
    print(result[0])
    if result[1]:
        find_synonym(synonym_dict)


num_of_pairs = int(input('Введите количество пар слов: '))
syn_dict = create_synonym_dict(num_of_pairs)
find_synonym(syn_dict)


