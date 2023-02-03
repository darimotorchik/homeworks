def find_wrong_cells(cells_list):
    wrong_cells = []
    for cell_index in range(len(cells_list)):
        if cells_list[cell_index] < cell_index:
            wrong_cells.append(cells_list[cell_index])
    print('\nНеподходящие значения: ', *wrong_cells)


cells_number = int(input('Кол-во клеток: '))
cells_user_list = []
for index in range(cells_number):
    cells_user_list.append(int(input(f'Эффективность {index + 1} клетки: ')))
find_wrong_cells(cells_user_list)
