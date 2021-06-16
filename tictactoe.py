print('Enter cells: ')
cells = input()

x = cells.count('X')
o = cells.count('O')
pl_x = 'X'
pl_o = 'O'


def print_cells(cell):
    print('---------')
    print('| ' + cell[0] + ' ' + cell[1] + ' ' + cell[2] + ' |')
    print('| ' + cell[3] + ' ' + cell[4] + ' ' + cell[5] + ' |')
    print('| ' + cell[6] + ' ' + cell[7] + ' ' + cell[8] + ' |')
    print('---------')


def check_winner(inp_data, player):
    # divide by rows
    rows = [inp_data[s:s + 3] for s in range(0, len(inp_data), 3)]

    # check rows
    for i in range(3):
        if rows[i].count(player) == 3:
            return 1

    # check columns
    for i in range(3):
        counter = 0
        for j in range(3):
            if rows[j][i] == player:
                counter += 1
        if counter == 3:
            return 1

    # check diagonals
    main_diag = rows[0][0] + rows[1][1] + rows[2][2]
    side_diag = rows[0][2] + rows[1][1] + rows[2][0]

    if main_diag.count(player) == 3 or side_diag.count(player) == 3:
        return 1

    return 0  # no win


print_cells(cells)

check_win_x = check_winner(cells, pl_x)
check_win_o = check_winner(cells, pl_o)

print(check_win_x)
print(check_win_o)

if abs(x - o) >= 2:
    print('Impossible')
elif check_win_x == 1 and check_win_o == 1:
    print('Impossible')
elif check_win_x == 1:
    print('X wins')
elif check_win_o == 1:
    print('O wins')
elif cells.count('_') == 0:
    print('Draw')
else:
    print('Game not finished')

print('Make the move!')

check = 0
while check == 0:
    print('Enter the coordinates: ')
    i, j = input().split()
    try:
        int(i)
        int(j)
    except ValueError:
        print('You should enter numbers!')
        continue
    else:
        if int(i) > 3 or int(j) > 3:
            print('Coordinates should be from 1 to 3!')
            continue

        index = (int(i) - 1) * 3 + int(j) - 1
        if cells[index] != '_':
            print('This cell is occupied! Choose another one!')
            continue

        cells = cells[:index] + 'X' + cells[index + 1:]
        print_cells(cells)
        check = 1
