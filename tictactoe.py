""" We will make the board using dictionary
    in which keys will be the location(i.e.top-left, mid-right, etc.) and initially it values will be empty space and then after every move we will change the value according to players choice of move."""

the_board={'7': ' ','8': ' ','9': ' ',
           '4': ' ','5': ' ','6': ' ',
           '1': ' ','2': ' ','3': ' '}

board_keys=[]

for key in the_board:
    board_keys.append(key)

"""WE will print the updated voard after every move in the game and thus we will make a funcition in which we will define the printboard function so that can easily print the board everytime by calling thus function.""" 

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn='X'
    count=0

    for i in range(10):
        printBoard(the_board)
        print("It's your turn, " + turn + ". Move to which place?")
            
        move=input()
        if the_board[move]==' ':
            the_board[move]=turn
            count+=1
        else:
            print("that place is already filled.\nMove to which place?")
            continue    

        if count>=5:
            if (the_board['7'] == the_board['8'] == the_board['9'] != ' ' or
                the_board['4'] == the_board['5'] == the_board['6'] != ' ' or 
                the_board['1'] == the_board['2'] == the_board['3'] != ' ' or 
                the_board['1'] == the_board['4'] == the_board['7'] != ' ' or 
                the_board['2'] == the_board['5'] == the_board['8'] != ' ' or 
                the_board['3'] == the_board['6'] == the_board['9'] != ' ' or 
                the_board['7'] == the_board['5'] == the_board['3'] != ' ' or 
                the_board['1'] == the_board['5'] == the_board['9'] != ' '):
                printBoard(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
        if count==9:
            print("Game is a tie!")

        if turn =='X':
            turn='O'
        else:
            turn="X"    

    restart=input("Do you want to play again? (y/n)")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            the_board[key]=" "

        game()

if __name__=="__main__":
    game()    
        