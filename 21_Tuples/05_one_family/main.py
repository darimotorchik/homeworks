families_data = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Петров', 'Алексей'): 42,
    ('Петрова', 'Юлия'): 38,
    ('Петрова', 'Анна'): 17,
    ('Васильев', 'Лев'): 28,
    ('Васильева', 'Алена'): 25,
    ('Васильев', 'Платон'): 1,
}

user_surname = input('Введите фамилию: ').strip().capitalize()
if user_surname[-1] == 'а':
    user_surname = user_surname[:-1]
result = tuple((person[0], person[1], age) for person, age in families_data.items()
               if user_surname in person[0])

for i_res in result:
    print(*i_res)
