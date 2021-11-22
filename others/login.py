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


class my_account():

    def __init__(self, save1='empty', save2='empty', save3='empty'):
        self.__save1 = save1
        self.__save2 = save2
        self.__save3 = save3
        self.list_new = [save1, save2, save3]

    def __str__(self):
        return f'save 1 : {self.save1}\nsave 2 : {self.save2}\nsave 3 : {self.save3}\n'

    @property
    def save1(self):
        return self.__save1

    @property
    def save2(self):
        return self.__save2

    @property
    def save3(self):
        return self.__save3

    @save1.setter
    def save1(self, save1):
        self.__save1 = save1

    @save2.setter
    def save2(self, save2):
        self.__save2 = save2

    @save3.setter
    def save3(self, save3):
        self.__save3 = save3


account = my_account()


def get_account():

    """
    read account from files

    """
    my_file = open('text/account_list').read().splitlines()
    return my_file


def set_account(lst):

    """
    set save 1 save 2 save 3 by username in database

    """

    account.save1 = lst[0]
    account.save2 = lst[1]
    account.save3 = lst[2]
    return account.save1, account.save2, account.save3


def check_duplicate(lst, user_input):

    """
    return true if the username is already exits in database

    >>> lst = ['jom','empty','empty']
    >>> user_input = 'jom'
    >>> check_duplicate(lst, user_input)
    True

    """
    for user in lst:
        if user == user_input:
            return True
        else:
            return False


def choose_save_space(num, name):

    """
    choose the account number and set it = to name

    """

    if num == '1':
        account.save1 = name
        return account.save1
    elif num == '2':
        account.save2 = name
        return account.save2
    elif num == '3':
        account.save3 = name
        return account.save3


def check_empty(lst, index):

    """
    check for empty save slot if save slot is not empty return False
    >>> lst = ['empty','empty','empty']
    >>> index = 1
    >>> check_empty(lst, index)
    True

    >>> lst = ['Jom','empty','empty']
    >>> index = 1
    >>> check_empty(lst, index)
    False

    """
    if lst[index - 1] != 'empty':
        return False
    elif lst[index - 1] == 'empty':
        return True


def login_main():

    """
    main function of module load used in main.py

    """

    username_lst = get_account()
    set_account(username_lst)
    print('Create a new account')
    print(account)
    save_space = input('Which save space (1,2,3) : ')

    if int(save_space) > 3 or int(save_space) < 1 :
        print('incorrect')

    if check_empty(username_lst,int(save_space)) == False:
        print('NOTE : This process is just only change the name,If you want to reset all information please delete the account')

    while True:
        name = input('Username : ')

        if check_duplicate(username_lst, name) == True:
            print('duplicate')

        else:
            choose_save_space(save_space, name)
            break
    print(account)


def main():

    print('------------------------------------------')
    login_main()

    write_my_file = open('text/account_list', 'w')
    write_my_file.writelines(f'{account.save1}\n')
    write_my_file.writelines(f'{account.save2}\n')
    write_my_file.writelines(f'{account.save3}\n')
    write_my_file.close()

















