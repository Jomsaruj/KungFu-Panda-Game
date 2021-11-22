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

from login import *
from Game_stat import *
import blackjack_oop
import Kungfu_panda_oop
import mancala_oop


def show_username(num):

    """
    print word 'hello' + account name

    """
    print()

    if num == '1':
        print(f'Hello {account.save1}')
    elif num == '2':
        print(f'Hello {account.save2}')
    elif num == '3':
        print(f'Hello {account.save3}')


def load_main():
    """
    main function of module load used in main.py

    """
    username_lst = get_account()
    set_account(username_lst)
    print('------------------------------------------')
    print(account)
    while True:
        choice_a = int(input('Choose your account (1,2,3) : '))
        if choice_a > 3:
            print('Maximum is 3')
        elif choice_a < 1:
            print('minimum is 1')
        elif username_lst[choice_a -1 ] == 'empty':
            print('This save is empty !')
        else:
            break

    show_username(choice_a)
    print('(1)Blackjack')
    print('(2)Mancala')
    print('(3)Kungfu panda')
    choice = int(input('Which game ? : '))
    if choice == 1:
        print('-' * 30)
        blackjack_oop.run(choice_a)
    elif choice == 2:
        print('-' * 30)
        mancala_oop.run(choice_a)

    elif choice == 3:
        print('-' * 30)
        po_score = Kungfu_panda_oop.run()
        Kungfu_panda_oop.report(choice_a, po_score)
    else:
        print('incorrect')




