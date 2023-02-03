phone_book = dict()

while True:
    print('Выберите действие: 1 - добавить контакт, 2 - поиск контакта по фамилии, любой символ - стоп')
    action = input()
    if action == '1':
        print('Добавление нового контакта')
        name = input('Введите имя: ').strip().capitalize()
        surname = input('Введите фамилию: ').strip().capitalize()
        person = (name, surname)
        if person in phone_book:
            print('Такой человек уже есть в вашей записной книжке')
        else:
            number = int(input('Введите номер телефона: '))
            phone_book[person] = number
        print('Имеющиеся контакты: ')
        print(phone_book)
        print()
    elif action == '2':
        searched_surname = input('Введите искомую фамилию: ').strip().capitalize()
        result = tuple((person[0], person[1], number) for person, number in phone_book.items()
                       if searched_surname in person)
        if not result:
            print('Такой фамилии еще нет в телефонной книге\n')
        else:
            for i_res in result:
                print(*i_res)
            print()
    else:
        print('\nЗавершение работы')
        break
