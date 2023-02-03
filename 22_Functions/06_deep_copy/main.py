def copy_function(template, name, active_sites):
    active_sites.append(template.replace('телефон', name))
    print(*active_sites, sep=2*'\n')


user_template = '''site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}'''

user_sites = []
user_num = int(input('Сколько сайтов: '))
for _ in range(user_num):
    user_prod = input('Введите название продукта для нового сайта: ')
    copy_function(user_template, user_prod, user_sites)
    print()
