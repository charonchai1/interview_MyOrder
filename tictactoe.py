import itertools
from tabnanny import check
from numpy import append



def win(current_game):

    def all_same(L):
        if L.count(L[0]) == len(L) and L[0] != 0:
            return True
        else:
            return False

     #TIE
    check = []
    for row in game:
        if(row.count(0)>0):
            check.append(row)
    if len(check)==0:
        print('DRAW!')
        return True
    

    #Horizontal
    for row in game:
        if all_same(row):
            if row[0] == 1:
                print(f"Player X is the winner")
            else:
                print(f"Player Y is the winner")
            return True

    #Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
            if diags[0] == 1:
                print("X  winner")
            else:
                print("Y  winner")
            return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
            if diags[0] == 1:
                print("X  winner")
            else:
                print("Y  winner")
            return True

    #Vertical
    for col in range(len(game)):
        check = []
        
        for row in game:
            check.append(row[col])
        if all_same(check):
            if check[0] == 1:
                print("X  winner")
            else:
                print("Y  winner")
            return True
    return False

   
    


def game_board(game_map, player=0 ,row=0, column=0, just_display=False):
    try:
        
        if game_map[row][column] != 0:
            print("this position is already choose")
            return game_map,False
        print("   0  1  2  NULL")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count,row)
        return game_map, True
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2".e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!",e)
        return game_map, False

play = True
player = [1,2]
while play:
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player : {current_player}")
        played = False
        
        while not played:
            column_choice = int(input("what column do you want to play? (0,1,2): "))
            row_choice = int(input("what row do you want to play? (0,1,2): "))
            game, played = game_board(game, current_player,row_choice,column_choice)
        if win(game):
            game_won = True
            again =  input("The game is over play again (y/n)?")
            if again.lower() == "y": 
                print("restarting")
            elif again.lower() == "n":
                print("close")
                play = False
            else:
                print("not a valid")
                play = False
            