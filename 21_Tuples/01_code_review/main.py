def find_interest_and_surname(user_dict):
    interests_list = []
    string_of_surnames = ''
    for id_person in user_dict:
        interests_list.extend(user_dict[id_person].get('interests'))
        string_of_surnames += user_dict[id_person].get('surname')
    return interests_list, len(string_of_surnames)


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

print('ID студента - возраст')
students_data_tuple = tuple(students.items())
for person in students_data_tuple:
    age = person[1].get('age')
    print(person[0], age, sep='  -  ')

interests, surname_len = find_interest_and_surname(students)
print('\nПолный список интересов всех студентов: ', end='')
print(*interests)
print(f'Общая длина всех фамилий студентов: {surname_len}', sep='\n')
