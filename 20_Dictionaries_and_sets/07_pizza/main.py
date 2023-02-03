num = int(input('Введите кол-во заказов: '))
result_dict = dict()
for i_num in range(1, num + 1):
    user_data_list = input(f'{i_num} заказ: ').split()
    name = user_data_list[0]
    pizza = user_data_list[1]
    quantity = int(user_data_list[2])
    if not result_dict.get(name):
        result_dict[name] = {pizza: quantity}
    elif not result_dict[name].get(pizza):
        result_dict[name][pizza] = quantity
    else:
        result_dict[name][pizza] += quantity

print()

for i_name in sorted(result_dict.keys()):
    print(i_name, ':', sep='')
    for i_pizza in sorted(result_dict[i_name].keys()):
        print(f'	    {i_pizza}: {result_dict[i_name][i_pizza]}')
