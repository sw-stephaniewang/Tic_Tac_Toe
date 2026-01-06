def show(grid):
    """Prints a tic tac toe grid"""
    print("+---+---+---+")
    for row in grid:
        print("|", end="")
        for cell in row:
            print(" " + cell + " |", end="")
        print("\n+---+---+---+")
    '''
    Print grid like this:
    +---+---+---+
    | X |   |   |
    +---+---+---+
    | O | X | X |
    +---+---+---+
    | O |   |   |
    +---+---+---+
    '''

def won(grid, player):
    """Checks if player supplied ('X' or 'O') won the game
      If so, returns True, otherwise returns False"""
    for row in grid:    # check rows
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    for col in range(3):    # check columns 3 times
        if grid [0][col] == player and grid [1][col] == player and grid [2][col] == player:
            return True

    # check 2 diagonals
    if grid [0] [0] == player and grid [1] [1] == player and grid [2] [2] == player:
        return True
    if grid [2] [0] == player and grid [1] [1] == player and grid [0] [2] == player:
        return True

    return False    # not win

def taken(grid, row, col):
    """Checks if the spot (row, col) on grid is available.
       Returns False if the spot on the grid is not taken,
       otherwise returns True"""
    if grid[row][col] == " ":   # spot available
        return False
    else:
        return True

def set_pos(grid, row, col, player):
    """Set a grid value at position row, col to player"""
    grid[row][col] = player

def read_pos(prompt):
    """Reads and returns a 0, 1, or 2 else forces a retry"""
    while True:
        try:
            user_input = int(input(prompt)) # read user input and convert to number
            if user_input == 0 or user_input == 1 or user_input == 2:
                return user_input
            else:
                print("Enter 0, 1, or 2")   # number not 0, 1, 2
        except ValueError:
            print("Enter 0, 1, or 2")   # input not integer

def main():
    """Implements a TicTacToe game"""
    grid = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    player = 'X'
    i = 0
    # There will be 9 maximum turns
    while i < 9:
        show(grid)
        print('Player', player)
        row = read_pos('row: ')
        col = read_pos('col: ')
        # skip current iteration spot taken
        if taken(grid, row, col):
            print('Spot taken! Try again.')
            continue
        # set position
        set_pos(grid, row, col, player)
        # check if player has won
        if won(grid, player):
            show(grid)
            print('Player', player, 'wins!')
            return
        # switch players
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        i = i + 1
    # nobody won
    print('It is a draw!')


if __name__ == "__main__":
    main()


