from itertools import product

def check_winner(board, player):
    """Check if a given player ('O' or 'X') has won the board."""
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6) 
    ]
    return any(all(board[i] == player for i in line) for line in winning_positions)

def is_valid_board(board):
    """Check if the given board state is valid."""
    count_O = board.count('O')
    count_X = board.count('X')

    
    if not (count_O == count_X or count_O == count_X + 1):
        return False

   
    O_wins = check_winner(board, 'O')
    X_wins = check_winner(board, 'X')

    if O_wins and X_wins:
        return False

    if O_wins and count_O == count_X:  
        return False
    if X_wins and count_O > count_X:  
        return False

    return True

def rotate_90(board):
    """Rotate a Tic-Tac-Toe board 90 degrees clockwise."""
    return [
        board[6], board[3], board[0],
        board[7], board[4], board[1],
        board[8], board[5], board[2]
    ]

def get_canonical_form(board):
    """Find the lexicographically smallest rotation of the board."""
    board_variants = [board]
    
    for _ in range(3):
        board = rotate_90(board)
        board_variants.append(board)
    
    return min(board_variants)

def generate_valid_boards():
    """Generate all valid Tic-Tac-Toe boards (ignoring rotations)."""
    valid_boards = set()
    
    for board_tuple in product(['O', 'X', '_'], repeat=9):
        board = list(board_tuple)

        if is_valid_board(board):
            canonical_board = tuple(get_canonical_form(board))
            valid_boards.add(canonical_board)

    return valid_boards

valid_board_states = generate_valid_boards()

print(f"Total valid unique Tic-Tac-Toe board states (ignoring rotations): {len(valid_board_states)}")
