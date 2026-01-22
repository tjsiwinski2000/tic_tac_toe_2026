#0121-2026-Udemy-Lesson86 [tic-tac-toe]
# human plays X and moves first; computer plays O , second

#initial position, constant for game restart
INITIAL_BOARD_POSITION =  ['-','-','-','-','-','-','-','-','-']

#all rows / columns, diagonals by designation
LIST_THREE_CONSECUTIVE =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def show_board(board):
    # print("\n")
    for count in range(0,9,3):
        print(f"{board[count]} | {board[count+1]}  | {board[count+2]}")
        
def move_is_legal(board,move):
    if move >= 0 and move <=8:
        if board_position[move]== '-':
            return True
        else:
            return False
    else:
        return False

def check_game_over(board,input_list):
    if board.count('-') == 0:
        print("Game is a tie.")
        return True #game over all squares filled
    
    #iterate thr. every combination [rows/columns/diagonals]
    for my_list in input_list:
        test_list=[]
        for position in my_list:
            test_list.append(board[position])
            #print(f"test_list in game over : {test_list}")
            if test_list.count('X') == 3:
                print("\nHuman you won *this* time.")
                return True #game over 
            if test_list.count('O') == 3:
                print("\nComputer has triumphed as expected ;-)")
                return True #game over 
    else:
        return False
    
def determine_computer_move(board):
    # FIRST. check if computer can WIN
    move = determine_two_row(LIST_THREE_CONSECUTIVE,"O")
    if move >= 0:
        return move
    # SECOND check if computer needs to BLOCK human from winning
    move = determine_two_row(LIST_THREE_CONSECUTIVE,"X")
    if move  >= 0:
        return move
    # THIRD cannot win AND nothing to block 
    # -- prioritize getting center,corner, then all other squares
    for num in (4,0,2,6,8,1,3,5,7):
        if move_is_legal(board,num):
            return(num) # take first available corner if !center

def determine_two_row(input_list,char):
    #iterate thr. every combination [rows/columns/diagonals] look for win/block
    for my_list in input_list:
        pos1 = my_list[0]
        pos2 = my_list[1]
        pos3 = my_list[2]
        test_list=[board_position[pos1],board_position[pos2],board_position[pos3]]
        #print(f"test_list= {test_list}")
        # two matching characters found, return position of BLOCK or WIN
        if test_list.count(char) == 2:
            if board_position[pos1] == '-':
                return pos1
            if board_position[pos2] == '-':
                return pos2
            if board_position[pos3] == '-':
                return pos3
        else:
            continue
    #reach here then there aren't any two in a row
    return -1
    
#display initial board
board_position = INITIAL_BOARD_POSITION 
show_board(board_position)
game_over = False

while not game_over:
    # human move portion
    if not game_over:
        move=int(input("what square do you want to move to?\n"))
        if move_is_legal(board_position,move) is False:
            print("Illegal move, please try again, remember squares are numbered 0 - 8 ")
            continue       
        board_position[move] ='X'
        show_board(board_position)
        game_over= check_game_over(board_position,LIST_THREE_CONSECUTIVE) 
    # computer move portion
    if not game_over:
        computer_move = int(determine_computer_move(board_position))
        board_position[computer_move] = 'O'
        game_over= check_game_over(board_position,LIST_THREE_CONSECUTIVE) 
        print("\n")
        show_board(board_position)