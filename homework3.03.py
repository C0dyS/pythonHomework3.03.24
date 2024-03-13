
def print_game(game_space):
    for i in range(3):
        for j in range(3):
            print(game_space[(i,j)], end=" ")
        print('')

def game_turn(game_space,symbol):
    try:
        x,y = map(int,input('please choose coordintaes x,y:').split())
        x -= 1
        y -= 1
        while not (-1 < x < 3 and -1 <= y < 3) or game_space.get((x,y)) != "*":
            print('wrong input')
            x, y = map(int, input('please choose coordintaes x,y:').split())
            x -= 1
            y -= 1
        game_space[x,y]=symbol
        return game_space
    except:
        print('ooops something went wrong,please try again')

def win_check(game_space):
    # Create a copy of the game_space dictionary
    game_space_copy = game_space.copy()

    for key in game_space_copy:
        if game_space_copy[key] == "x":
            game_space_copy[key] = 1
        elif game_space_copy[key] == '0':
            game_space_copy[key] = -1
        else:
            game_space_copy[key] = 0

    win_var = False
    win_x_0 = False
    if game_space_copy[(0, 0)] + game_space_copy[(1, 1)] + game_space_copy[(2, 2)] == 3:
        win_var = True
        win_x_0 = True
    elif game_space_copy[(0, 0)] + game_space_copy[(1, 1)] + game_space_copy[(2, 2)] == -3:
        win_var = True
        win_x_0 = False
    if game_space_copy[(0, 2)] + game_space_copy[(1, 1)] + game_space_copy[(2, 0)] == 3:
        win_var = True
        win_x_0 = True
    elif game_space_copy[(0, 2)] + game_space_copy[(1, 1)] + game_space_copy[(2, 0)] == -3:
        win_var = True
        win_x_0 = False


    for i in range(3):
        sum_check_row = 0
        sum_check_column = 0
        for j in range(3):
            sum_check_row += game_space_copy[(i,j)]
            sum_check_column += game_space_copy[(j,i)]
            if sum_check_row == 3:
                win_var = True
                win_x_0 = True
            elif sum_check_row == -3:
                win_var = True
                win_x_0 = False
            if sum_check_column == 3:
                win_var = True
                win_x_0 = True
            elif sum_check_column == -3:
                win_var = True
                win_x_0 = False

    return win_var,win_x_0





def game():
    game_space = {(i,j): "*" for i in range(3) for j in range(3)}
    print_game(game_space)
    turn_check = 1
    symbol = '0'
    while True:
        turn_check += 1
        if turn_check % 2 == 0:
            symbol = '0'
        else:
            symbol = 'x'
        print(f"turn number : {turn_check - 1}, its {symbol}'s turn")
        print("game field:")
        print_game(game_space)
        game_space = game_turn(game_space,symbol)
        print_game(game_space)
        game_space_2 = game_space
        win_var,win_x_0 = win_check(game_space_2)
        if win_var == True:
            if win_x_0 == True:
                print('game over, x wins')
                break
            elif win_x_0 == False:
                print('game over, 0 wins')
                break
        elif win_var == False:
            continue


game()

