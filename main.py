import sys
sys.path.insert(1, 'Game')
sys.path.insert(1, 'others')
sys.path.insert(1, 'text')
sys.path.insert(1, 'Game/game1')
sys.path.insert(1, 'Game/game2')
sys.path.insert(1, 'Game/game3')
sys.path.insert(1, 'others/login')
sys.path.insert(1, 'others/load')
sys.path.insert(1, 'others/Delete')
sys.path.insert(1, 'others/Game_stat')
sys.path.insert(1, 'others/player')
sys.path.insert(1, 'text/account_list')
sys.path.insert(1, 'text/balance.txt')
sys.path.insert(1, 'text/blackjack_play')
sys.path.insert(1, 'text/blackjack_win')
sys.path.insert(1, 'text/kungfupanda_play')
sys.path.insert(1, 'text/kungfupanda_win')
sys.path.insert(1, 'text/mancala_play')
sys.path.insert(1, 'text/mancala_win')


import login
import load
import Delete
import Game_stat
import player


while True:

    begin = input('(N)ewgame , (L)oad , (R)anking , (D)elete , (Q)uit : ').lower()
    player1, player2, player3 = player.main()
    player1_game1, player1_game2, player1_game3 = Game_stat.main(1)
    player2_game1, player2_game2, player2_game3 = Game_stat.main(2)
    player3_game1, player3_game2, player3_game3 = Game_stat.main(3)

    if begin == 'n':

        login.main()

    elif begin == 'l':
        count = 0
        player_list = login.get_account()
        for i in player_list:
            if i == 'empty':
                count += 1
        if count == 3:
            print("You need to create at least one account(please enter 'n')")
            print()
        else:
            load.load_main()

    elif begin == 'r':
        print()
        print(player1)
        print(f'{player1_game1}\n{player1_game2}\n{player1_game3}\n')

        print(player2)
        print(f'{player2_game1}\n{player2_game2}\n{player2_game3}\n')

        print(player3)
        print(f'{player3_game1}\n{player3_game2}\n{player3_game3}\n')

    elif begin == 'd':
        Delete.main()

    elif begin == 'q':
        break

    else:
        print('You must enter only (n,l,r,d,q)')
        print('Please try again !')


