friends = int(input('Кол-во друзей: '))
IOU = int(input('Долговых расписок: '))
friends_list = list(range(1, friends + 1))
friends_balance = [0 for _ in range(friends)]
IOU_form = []

for i_iou in range(1, IOU + 1):
    print(f'\n{i_iou} расписка')
    IOU_form.append(int(input('Кому: ')))
    IOU_form.append(int(input('От кого: ')))
    IOU_form.append(int(input('Сколько: ')))
    friends_balance[IOU_form[0] - 1] -= IOU_form[-1]
    friends_balance[IOU_form[1] - 1] += IOU_form[-1]
    IOU_form.clear()

print('\nБаланс друзей:')
for i_fr in range(1, friends + 1):
    print(f'{i_fr} : {friends_balance[i_fr - 1]}')
