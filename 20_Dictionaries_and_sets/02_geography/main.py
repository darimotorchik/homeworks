number = int(input('Кол-во стран: '))
country_city_dict = dict()

for num in range(1, number + 1):
    city_list = input(f'{num} страна: ').title().split()
    for cities in city_list[1:]:
        country_city_dict[cities] = f'Город {cities} расположен в стране {city_list[0]}'

for i_city in range(1, 4):
    city = input(f'\n{i_city} город: ').capitalize()
    result = country_city_dict.get(city, f'По городу {city} данных нет.')
    print(result)
