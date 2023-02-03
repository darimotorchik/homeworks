films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favourite_films = []
number_of_films = int(input('Сколько фильмов хотите добавить? '))
for _ in range(number_of_films):
    film = input('Введите название фильма: ')
    if film in films:
        favourite_films.append(film)
    else:
        print(f'Ошибка: фильма {film} у нас нет :(')
print('Ваш список любимых фильмов: ', end='')
print(*favourite_films, sep=', ')
