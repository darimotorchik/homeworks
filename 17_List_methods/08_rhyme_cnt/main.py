members = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number} человек')
members_list = list(range(1, members + 1))
start_index = 0
start_member = members_list[start_index]

while len(members_list) > 1:
    print(f'\nТекущий круг людей: {members_list}')
    print(f'Начало счёта с номера {start_member}')
    if number > len(members_list):
        if number == len(members_list) + 1:
            loser_member = start_member
        elif start_member == members_list[-1]:
            loser_member = members_list[number % len(members_list) - 2]
        else:
            loser_member = members_list[number % len(members_list) + start_index - 1]
    else:
        if number > len(members_list) - start_index:
            loser_member = members_list[number - (len(members_list) - start_index) - 1]
        else:
            loser_member = members_list[number - 1 + start_index]
    print(f'Выбывает человек под номером {loser_member}')
    loser_index = members_list.index(loser_member)
    if loser_index < len(members_list) - 1:
        start_member = members_list[loser_index + 1]
    else:
        start_member = members_list[0]
    members_list.remove(loser_member)
    start_index = members_list.index(start_member)
print(f'\nОстался человек под номером {members_list[0]}')
