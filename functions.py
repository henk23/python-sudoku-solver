from colorama import Fore

CURSOR_UP = '\033[F'
ERASE_LINE = '\033[K'


def list_unique(l):
    nums = []
    for num in l:
        if num != 0:
            if num in nums:
                return False
            else:
                nums.append(num)
    return True


def valid_row(sudoku, row_idx):
    row = sudoku[row_idx]
    return list_unique(row)


def valid_col(sudoku, col_idx):
    col = []
    for i in range(9):
        col.append(sudoku[i][col_idx])
    return list_unique(col)


def valid_square(sudoku, square_nr):
    square = []

    square_x, square_y = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)][square_nr]

    for y in range(square_y * 3, square_y * 3 + 3):
        for x in range(square_x * 3, square_x * 3 + 3):
            square.append(sudoku[y][x])
    return list_unique(square)


def print_matrix(sudoku, predefined):
    for x, row in enumerate(sudoku):
        for y, val in enumerate(row):

            if predefined[x][y]:
                print(Fore.CYAN, end='')

            if (y + 1) % 3:
                print('{:2}'.format(val), end='')
            else:
                print('{:2}'.format(val), end=' ')

            print(Fore.RESET, end='')

        if (x + 1) % 3:
            print('', end='\n')
        else:
            print('', end='\n\n')


def increase_x(x, y):
    x += 1
    if x > 8:
        x = 0
        y += 1
    return x, y


def decrease_x(x, y):
    x -= 1
    if x < 0:
        x = 8
        y -= 1
    return x, y

