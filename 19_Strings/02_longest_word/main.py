user_string = input('Введите строку: ')
word_list = user_string.split(' ')
len_list = [len(word_list[word_i]) for word_i in range(len(word_list))]
max_len, max_word = max(len_list), word_list[len_list.index(max(len_list))]
print(f'Самое длинное слово: {max_word}', f'Длина этого слова: {max_len}', sep='\n')
