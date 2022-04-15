a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))

first_player = False
second_player = False

game = [a, b, c]

if game[0][0] == game[0][1] == game[0][2] == 1 or game[1][0] == game[1][1] == game[1][2] == 1 or game[2][0] \
        == game[2][1] == game[2][2] == 1 or game[0][0] == game[1][0] == game[2][0] == 1 or \
        game[0][1] == game[1][1] == game[2][1] == 1 or game[0][2] == game[1][2] == game[2][2] == 1 or \
        game[0][0] == game[1][1] == game[2][2] == 1 or game[0][2] == game[1][1] == game[2][0] == 1:
    first_player = True
elif game[0][0] == game[0][1] == game[0][2] == 2 or game[1][0] == game[1][1] == game[1][2] == 2 or game[2][0] \
        == game[2][1] == game[2][2] == 2 or game[0][0] == game[1][0] == game[2][0] == 2 or \
        game[0][1] == game[1][1] == game[2][1] == 2 or game[0][2] == game[1][2] == game[2][2] == 2 or \
        game[0][0] == game[1][1] == game[2][2] == 2 or game[0][2] == game[1][1] == game[2][0] == 2:
    second_player = True

if first_player:
    print('First player won')
elif second_player:
    print('Second player won')
else:
    print('Draw!')
