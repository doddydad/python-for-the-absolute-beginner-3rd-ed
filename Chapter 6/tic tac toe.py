#tic-tac-toe

import random

#global constants

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#definitions

def display_instruct():
    """display game instructions"""
    print(
"""
Welcome to the greatest intellectual showdown of all time: Tic-Tac-Toe
This will be a showdown between your human brain and my silicon processor.

You will make your move by entering a number, 0 - 8. The number
will correspond to the board positions as illustrated:

            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8

Prepare yourself human, the ultimate battle is about to begin
\n""")

def new_board():
    """creates a new board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display the board on screen"""
    print("\n\t", board[0], "|", board[1],"|",board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    """Create list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def ask_yes_no(question):
    """asks a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question = "", low = 0, high = 10, step = 1):
    """asks for a number"""
    response = None
    while response not in range(low,high,step):
        try:
            response = int(input(question))
        except ValueError:
            print("This isn't a whole number")
    return response

#Who goes first and what pieces they have
def pieces():
    """determine if computer or human goes first. Also assigns pieces"""
    go_first = ask_yes_no("Do you require the first move? (y/n):")
    if go_first == "y":
        print("\n Then take the first move, you'll need it.")
        human = X
        computer = O
    elif go_first == "n":
        print("\n foolish mortal, I shall go first")
        human = O
        computer = X
    return computer, human

def winner(board):
    """Check if someone won"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    """get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied foolish mortal, try again")
    print("Acceptable")
    #global board[move] = human  other way of doing it I think
    return move


#computer's choice
def best_computer_move(board, computer, human): 
    """Third Iteration, now unbeatable"""
    
    #Definitions
    CORNERS = (0, 6, 8, 2)
    candidates = []
    moves = legal_moves(board)
    board = board[:]

    #specific check against corner strategy
    if board[4] == computer:                    
        if board[0] == human == board[8] or board[2] == human == board[6]:
            if board[1] == board[3] == board[5] == board[7] == EMPTY:
                move = random.choice((1,3,5,7))
                return move
            
    #checks if it can win this turn        
    for move in moves:                          
        board[move] = computer                  
        if winner(board) == computer:
            return move
        board[move] = human 
        
        #check to prevent human winning next turn
        if winner(board) == human:              
            candidates.append(move)
        board[move] = EMPTY
    if candidates:
        move = random.choice(candidates)
        return move
    
    #This block chooses best generic move
    if 4 in moves:                              
        return 4
    for move in CORNERS:                        
        if move in moves:
            candidates.append(move)
    #randomises which corner, seems like it's more different
    if candidates:                              
        move = random.choice(candidates)
        return move
    move = random.choice(moves)
    return move

def next_turn(turn):
    """Switch turns"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, human, computer):
    """Congratulate the winner"""
    if the_winner != TIE:
        if the_winner == human:
            print("The damned human won")
        else:
            print("I am supreme")
    else:
        print("It's a tie")

    if the_winner == computer:
        print("Get rekt you filthy casual")
    
    #genuinely should never appear    
    elif the_winner == human:               
        print("Impossible, how could this happen")

    elif the_winner == TIE:
        print("You were lucky to get away so easily that time")

def main():
    """we can nest things lots"""
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        elif turn == computer:
            move = best_computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, human, computer)

#the program

main()
input()
