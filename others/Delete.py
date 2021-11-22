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
sys.path.insert(1, 'others/player_handle')
sys.path.insert(1, 'text/account_list')
sys.path.insert(1, 'text/balance.txt')
sys.path.insert(1, 'text/blackjack_play')
sys.path.insert(1, 'text/blackjack_win')
sys.path.insert(1, 'text/kungfupanda_play')
sys.path.insert(1, 'text/kungfupanda_win')
sys.path.insert(1, 'text/mancala_play')
sys.path.insert(1, 'text/mancala_win')

import Game_stat
import player
from login import account, get_account, set_account
from player_handle import *


def main():
    player1, player2, player3 = player.main()
    player1_game1, player1_game2, player1_game3 = Game_stat.main(1)
    player2_game1, player2_game2, player2_game3 = Game_stat.main(2)
    player3_game1, player3_game2, player3_game3 = Game_stat.main(3)

    username_lst = get_account()
    set_account(username_lst)
    print('------------------------------------------')
    print(account)

    choice = int(input('Which save do you want to delete (1),(2),(3) : '))
    if choice == 1:
        account.save1 = 'empty'
        player1.balance = 1000
        player1_game1.num_plays = 0
        player1_game1.num_wins = 0
        player1_game2.num_plays = 0
        player1_game2.num_wins = 0
        player1_game3.num_plays = 0
        player1_game3.num_wins = 0
        print('Save 1 removed')

    elif choice == 2:

        account.save2 = 'empty'
        player2.balance = 1000
        player2_game1.num_plays = 0
        player2_game1.num_wins = 0
        player2_game2.num_plays = 0
        player2_game2.num_wins = 0
        player2_game3.num_plays = 0
        player2_game3.num_wins = 0
        print('Save 2 removed')

    elif choice == 3:

        account.save3 = 'empty'
        player3.balance = 1000
        player3_game1.num_plays = 0
        player3_game1.num_wins = 0
        player3_game2.num_plays = 0
        player3_game2.num_wins = 0
        player3_game3.num_plays = 0
        player3_game3.num_wins = 0
        print('Save 3 removed')

    import_class = PlayerHandler()
    import_class.write_to_file('text/account_list', account.save1, account.save2, account.save3)
    import_class.write_to_file('text/balance.txt', player1.balance, player2.balance, player3.balance)

    import_class.write_to_file('text/blackjack_play', player1_game1.num_plays, player2_game1.num_plays, player3_game2.num_plays)
    import_class.write_to_file('text/blackjack_win', player1_game1.num_wins, player2_game1.num_wins, player3_game2.num_wins)

    import_class.write_to_file('text/kungfupanda_play', player1_game1.num_plays, player2_game1.num_plays,player3_game2.num_plays)
    import_class.write_to_file('text/kungfupanda_win', player1_game1.num_wins, player2_game1.num_wins, player3_game2.num_wins)

    import_class.write_to_file('text/mancala_play', player1_game1.num_plays, player2_game1.num_plays,player3_game2.num_plays)
    import_class.write_to_file('text/mancala_win', player1_game1.num_wins, player2_game1.num_wins, player3_game2.num_wins)











