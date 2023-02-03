def create_num_seqs(num):
    if num == 1:
        return 1
    elif num == 2:
        return [num, create_num_seqs(num - 1)]
    return [num, *create_num_seqs(num - 1)]


user_number = int(input('Введите число: '))
user_seq = create_num_seqs(user_number)
print()
for i_el in user_seq[::-1]:
    print(i_el)

