strings_num = int(input('Сколько записей вносится в протокол? '))
players_data = {}
for order in range(1, strings_num + 1):
    score, name = tuple(input(f'{order} запись: ').split())
    score = int(score)
    is_it_already_added = players_data.get(name)
    if is_it_already_added and is_it_already_added[1] >= score:
        continue
    players_data[name] = (order, score)
print('\nИтоги соревнований:')
result = sorted(players_data.items(), key=lambda x: (-x[1][1], x[1][0]))
for place, data in enumerate(result[:3]):
    print(f'{place + 1} место. {data[0]} ({data[1][1]})')
