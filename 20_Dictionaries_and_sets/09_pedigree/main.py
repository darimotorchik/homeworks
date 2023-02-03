people_num = int(input('Введите количество человек: '))
pedigree_dict = dict()

for i_pair in range(1, people_num):
    pair = input(f'{i_pair} пара: ').split()
    if i_pair == 1:
        head = pair[1]
        pedigree_dict[head] = 0
    parents_num = pedigree_dict.get(pair[1])
    pedigree_dict[pair[0]] = parents_num + 1

print('\n“Высота” каждого члена семьи:')
for i_mem in sorted(pedigree_dict):
    print(i_mem, pedigree_dict[i_mem])
