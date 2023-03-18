import math
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def tic_tac_toe_game():
    not_3_in_a_row = True
    moves = 0
    x_moves = []
    o_moves = []
    board = ' |1|2|3| \n |4|5|6| \n |7|8|9| '
    while not_3_in_a_row and moves < 9:
        current_turn = 'x' if moves % 2 == 0 else 'o'
        print(moves, current_turn)
        moves += 1
        print(board)
        space = int(input('Which space would you like to place? ')) -1
        board = board.replace(str(space +1), current_turn)
        x_moves.append([space//3, space%3]) if current_turn == 'x' else o_moves.append([space//3, space%3])
        print(x_moves,o_moves)
        if '1' in x_moves and '2' in x_moves and '3' in x_moves:
            return 'x wins'
    else:
        return 'It\'s a draw'
print(tic_tac_toe_game())



