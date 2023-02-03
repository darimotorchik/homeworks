violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_number = int(input('Сколько песен выбрать? '))
select_song_set = {violator_songs.get(input(f'Название {num} песни: ')) for num in range(1, songs_number + 1)}
if (len(select_song_set) < songs_number) or (None in select_song_set):
    print('Ошибка! Среди запрошенных песен есть или несуществующие песни в исходном списке, либо повторы')
else:
    print(f'Общее время звучания песен: {sum(select_song_set)} минут')
