import time
# Easy Board: 
# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

# Very Hard Board:
board = [
    [0,0,6,0,0,8,0,0,0],
    [0,0,0,0,0,1,0,9,0],
    [2,0,0,9,6,0,7,0,0],
    [0,0,0,1,0,0,0,0,0],
    [0,0,4,2,9,0,0,5,0],
    [0,5,0,0,0,0,8,0,0],
    [0,0,0,0,0,6,0,0,0],
    [7,0,0,0,0,0,0,0,3],
    [0,0,2,5,4,0,0,8,7]
]

def print_board(board): 
    """
    print suduko board 
    Args:
        board (2d-array): board to print
    """
    count = 0
    print(f"\n")
    for row in board:
        i = 0
        while i < 9: 
            print(f" {row[i]}   {row[i+1]}   {row[i+2]} ", end='')
            if i != 6:
                print("|", end="")
            i += 3
            
        count += 1
        if count % 3 == 0 and count != 9:
            print(f"\n - - - - - - - - - - - - - - - - - ")
        else: 
            print("\n")
        

def find_empty(board): 
    """ 
    find the first empty square denoted by 0 in the board
    Args:
        board (2d-array): board to solve
    Returns:
        _type_: list, (row, column) if empty square found else returns None
    """
    
    for row in range(len(board)): 
        for column in range(len(board[row])): 
            if board[row][column] == 0: 
                return [row, column]
            
    return None
               
def check_entry_valid(board, value, position):
    """check row, column and square if value you want to enter is valid
    Args:
        board (2d-array): board to check
        value (int): value to enter
        position (array): position to insert the value [row,column]
        
    Return: Boolean, True if entry is valid else false
    """
    #print(position)
    row = position[0]
    column = position[1]
    
    # check row
    for i in range(len(board[row])):
        if board[row][i] == value: 
            return False
    
    # check column
    for i in range(len(board[column])):
        if board[i][column] == value: 
            return False
    
    # check square
    # find square to check
    i = row // 3
    j = column // 3
    check_row = i*3 
    check_column = j*3

    while check_row // 3 == i: 
        while check_column // 3 == j:
            if board[check_row][check_column] == value: 
                return False
            check_column += 1
        
        # reset column to set at beginning of square when incrementing row    
        check_column = j*3
        check_row += 1
         
    return True

def solve(board): 
    """
    Uses backtracking algorthim
    1. Find empty squre, if none then you know you're done!
    2. From valid values (1-9) go through and find the first valid value
    3. Call solve again
    4. if invalid value is found it will set to 0 and return False
        this will then reassign the last set square to the next valid value
        if there is one. Else it will set to 0 and go back again. Reset a value 
        then continue forward again until the board is solved. 
    """
    # once filled last square, done solving 
    empty_square = find_empty(board)
    
    if empty_square is None:
        return True
    else: 
        pos = empty_square
    
    # recursively solve board until no more empty squares
    for i in range(1,10): 
        if check_entry_valid(board, value=i, position=pos):
            board[pos[0]][pos[1]] = i
            if solve(board): 
                return True
            
            board[pos[0]][pos[1]] = 0
            
    return False
            
if __name__ == "__main__":
    print_board(board)
    start_time = time.time()
    solve(board)
    end_time = time.time()
    total_time = end_time-start_time
    print(f"\nSolved Board in {int(total_time)} seconds:", end="")
    print_board(board)