goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

result = dict()
for i_goods in goods:
    num = goods[i_goods]
    total_quantity = 0
    total_price = 0
    for items in store[num]:
        total_quantity += items['quantity']
        total_price += items['price'] * items['quantity']
    result[i_goods] = [total_quantity, total_price]

for i_res in result:
    print(f'{i_res} - {result[i_res][0]} шт, стоимость {result[i_res][1]} руб')
