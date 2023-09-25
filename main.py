import sys


class Game():
    def __init__(self):
        pass

    # Printing game grid
    def print_grid(self, symbols):

        print("---------")
        print("| {} {} {} |".format(symbols[0], symbols[1], symbols[2]))
        print("| {} {} {} |".format(symbols[3], symbols[4], symbols[5]))
        print("| {} {} {} |".format(symbols[6], symbols[7], symbols[8]))
        print("---------")

    # Game status check

    def game_result(self, symbols):
        matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        win = False

        for el in range(len(matrix)):
            first_el = matrix[el][0]
            second_el = matrix[el][1]
            third_el = matrix[el][2]

            if symbols[first_el] == "X" and symbols[second_el] == "X" and symbols[third_el] == "X":
                print("X wins")
                win = True
                return win

            elif symbols[first_el] == "O" and symbols[second_el] == "O" and symbols[third_el] == "O":
                print("O wins")
                win = True
                return win

        if not win:
            if '_' not in symbols:
                print("Draw")
                return True
            elif '_' in symbols and abs(symbols.count("X") - symbols.count("O")) <= 1:
                print("Game not finished")
                return False
            else:
                print("Impossible")
                return True


grid = list("_________")

tic_tac_toe = Game()
tic_tac_toe.print_grid(grid)

game_status = False
status = "first_player"
grid_list = list(grid)
while not game_status:
    user_move = input("Please enter 2 numbers that represent the cell: ").split(" ")

    # Checking the correctness of data entry
    if len(user_move) != 2:
        print("You should enter TWO numbers!")
        continue

    if not user_move[0].isdigit() or not user_move[1].isdigit():
        print("You should enter numbers!")
        continue

    user_move = list(map(int, user_move))

    if user_move[0] not in (1, 2, 3) or user_move[1] not in (1, 2, 3):
        print("Coordinates should be from 1 to 3!")
        continue

    # Formula to match the user_move to the cell number in a grid
    index = (user_move[0] - 1) * 3 + user_move[1] - 1

    # Checking if the cell number in a grid is occupied or not. If not, make a move
    if grid[index] != '_':
        print("This cell is occupied! Choose another one!")
        continue
    if status == "first_player":
        grid_list[index] = 'X'
        tic_tac_toe.print_grid(grid_list)
        game_status = tic_tac_toe.game_result(grid_list)
        status = "second_player"
        continue
    if status == "second_player":
        grid_list[index] = 'O'
        tic_tac_toe.print_grid(grid_list)
        game_status = tic_tac_toe.game_result(grid_list)
        status = "first_player"
        continue

