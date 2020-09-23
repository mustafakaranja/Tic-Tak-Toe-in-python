#!/usr/bin/env python
# coding: utf-8

# In[2]:


print ("Author name : Mustafa yusuf karanjawala")


# In[2]:


def print_board(board):
    print(' '+board[7]+'  |'+' '+board[8]+'  |'+' '+board[9])
    print('----|----|---')
    print(' '+board[4]+'  |'+' '+board[5]+'  |'+' '+board[6])
    print('----|----|---')
    print(' '+board[1]+'  |'+' '+board[2]+'  |'+' '+board[3])


# In[3]:


test_board = ['#','X','O','X','O','X','X','O','X','O']
print_board(test_board)


# In[4]:


#now we have to add the input choose for the player 1 and player 2 
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
          marker = input ("Player 1, please input the 'X' or 'O': ")
    player1 = marker
            
#now we give the choise actionn to the each player which the have taken
    
    if player1 == 'X':
        player2 = 'O'
        print (f'the marker of player1 is {player1}, and player2 is {player2}')
    else:
        player2 = 'X'
        print (f'the marker of player1 is {player1}, and player2 is {player2}')
    return player1,player2   


# In[5]:


player_input()


# In[6]:


def input_value(board,value,position):
    board[position] = value


# In[7]:


# define the fuction which says the win condition
def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark) or
            (board[4]==board[5]==board[6]==mark) or
            (board[7]==board[8]==board[9]==mark) or
            (board[1]==board[5]==board[9]==mark) or
            (board[7]==board[5]==board[3]==mark))


# In[8]:


#define the fuction which gives the option to player to whoom want to play first
import random
def choose_first():
    flip = random.randint(0,1)
    
    if flip == 1:
        return 'play player 1'
    else:
        return 'play player 2'


# In[9]:


#define the function which return the bolean value cheching if the index is empty or full
def space_check(board,position):
    return board[position] == ' '


# In[10]:


#define the function which is return the bolean if the board is full 
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
#showing full box
    return True


# In[11]:


#ask the player for the postion to enter in the board
def player_choice(board):
    position = 0
    while position not in (1,2,3,4,5,6,7,8,9) or not space_check(board,position):
            position = int(input ( 'Choose the postion in (1-9)'))
    return position


# In[12]:


def relay():
    choice = input ("If you play the game again say 'yes'or 'no'")
    return choice


# In[ ]:


#while loop 
print (' wellcome to my first game Name :tic tac toe')

while True:
    #play game
    ##set everything up (board, whoes turn ,choose marker )
    
    the_board = [' ']*10
    player1,player2 = player_input()
    
    turn = choose_first()
    print (turn + ' will go first')
    
    play_game = input ('ready to play? say y or n')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    #game play
    while game_on:
         
            if turn == 'player1':
                #show the board
                print_board(the_board)
                #choose the possion
                position = player_choice(the_board)
                #place the marker
                input_value(the_board,player1,position)
            #win condition
                if win_check(the_board,player1):
                    print_board(the_board)
                    print (" Player 1 Win the match ")
                    game_on = False
                # check if else is is the tie or not
                else:
                    if full_board_check(the_board):
                        print_board(the_board)
                        print (" Game is tie")
                        game_on = False
                    else:
                        turn = 'player2'
                    
            #check if the there is a tie
            else:
                print_board(the_board)
                #choose the possion
                position = player_choice(the_board)
                #place the marker
                input_value(the_board,player2,position)
            #win condition
                if win_check(the_board,player2):
                    print_board(the_board)
                    print (" Player 2 Win the match ")
                    game_on = False
                # check if else is is the tie or not
                else:
                    if full_board_check(the_board):
                        print_board(the_board)
                        print (" Game is tie")
                        game_on = False
                    else:
                        turn = 'player1'
    


# In[ ]:




