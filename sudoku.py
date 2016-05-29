from functions import *

print("Please enter the rows of the sudoku. Use zero (0) for empty fields. Use space as a delimiter.")

sudoku = list(range(9))
for i in range(9):
    sudoku[i] = input("row " + str(i + 1) + ": ").split()
    for idx, val in enumerate(sudoku[i]):
        sudoku[i][idx] = int(sudoku[i][idx])

print("\nCalculating...\n")

predefined = [[False for i in range(9)] for j in range(9)]

for x in range(9):
    for y in range(9):
        if sudoku[y][x] != 0:
            predefined[y][x] = True

print_matrix(sudoku, predefined)
print("\n")

try_nr = [[1 for k in range(9)] for l in range(9)]
current_x = 0
current_y = 0

while predefined[current_y][current_x]:
    current_x, current_y = increase_x(current_x, current_y)
    if current_y > 8:
        print("sudoku seems to be solved already...")
        print_matrix(sudoku, predefined)
        exit()

while True:

    sudoku[current_y][current_x] = try_nr[current_y][current_x]

    valid = True
    for i in range(9):
        valid = valid and valid_row(sudoku, i) and valid_col(sudoku, i) and valid_square(sudoku, i)

    if valid:
        current_x, current_y = increase_x(current_x, current_y)
        if current_y > 8:
            print("finished.\n")
            print_matrix(sudoku, predefined)
            exit()
        while predefined[current_y][current_x]:
            current_x, current_y = increase_x(current_x, current_y)
            if current_y > 8:
                print("finished.\n")
                print_matrix(sudoku, predefined)
                exit()
    else:
        while True:
            if try_nr[current_y][current_x] == 9:
                try_nr[current_y][current_x] = 1
                sudoku[current_y][current_x] = 0
                current_x, current_y = decrease_x(current_x, current_y)
                if current_y < 0:
                    print("not solvable\n")
                    print_matrix(sudoku, predefined)
                    exit()
                while predefined[current_y][current_x]:
                    current_x, current_y = decrease_x(current_x, current_y)
                    if current_y < 0:
                        print("not solvable\n")
                        print_matrix(sudoku, predefined)
                        exit()
            else:
                try_nr[current_y][current_x] += 1
                break
