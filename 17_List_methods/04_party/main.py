guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
user_answer = ''

while user_answer != 'пора спать':
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    user_answer = input('Гость пришел или ушел? ').lower()
    if user_answer == 'пора спать':
        continue
    name = input('Имя гостя: ')
    if user_answer == 'пришел' and len(guests) < 6:
        guests.append(name)
        print(f'Привет, {name}!')
    elif user_answer == 'пришел' and len(guests) >= 6:
        print(f'Прости, {name}, но мест нет.')
    elif user_answer == 'ушел' and name in guests:
        guests.remove(name)
        print(f'Пока, {name}!')
    elif user_answer == 'ушел' and name not in guests:
        print('Этого гостя сейчас нет на вечеринке и он не может уйти')
else:
    print('Вечеринка закончилась, все легли спать.')
