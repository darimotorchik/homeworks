special_sym = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
file_end = ('.txt', '.docx')
file_title = input('Название файла: ')
if file_title.startswith(special_sym):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_title.endswith(file_end):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')
