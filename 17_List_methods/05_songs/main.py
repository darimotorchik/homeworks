violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

result_time = 0
num_songs = int(input('Сколько песен выбрать? '))
for i_song in range(1, num_songs + 1):
    song = input(f'Название {i_song} песни: ')
    for j_song in range(len(violator_songs)):
        if violator_songs[j_song][0] == song:
            result_time += violator_songs[j_song][1]
print(f'Общее время звучания песен: {round(result_time, 2)} минут')
