shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

user_detail = input('Название детали: ')
item_result = 0
price = 0

for i_item in shop:
    if i_item.count(user_detail):
        price += i_item[1]
        item_result += i_item.count(user_detail)

print(f'Кол-во деталей - {item_result}', f'Общая стоимость - {price}', sep='\n')
