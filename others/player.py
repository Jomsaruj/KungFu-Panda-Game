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

from player_handle import *
import Game_stat


class Player():

    def __init__(self, player_name='_', balance=1000, game_stat_list = '_'):
        self.__player_name = player_name
        self.__balance = balance
        self.__game_stat_list = game_stat_list

    def __str__(self):
        return f'{self.__player_name}: Balance = {self.__balance}'

    @property
    def player_name(self):
        return self.__player_name

    @property
    def balance(self):
        return self.__balance

    @property
    def game_stat_list(self):
        return self.__game_stat_list

    @player_name.setter
    def player_name(self, player_name):
        self.__player_name = player_name

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @game_stat_list.setter
    def game_stat_list(self, game_stat_list):
        self.__game_stat_list = game_stat_list


    def update_num_plays(self,player,num_play):

        """
        if the game is active this function will add num_play by 1


        """
        if player == 1:
            num_play += 1
        elif player == 2:
            num_play += 1
        elif player == 3:
            num_play += 1
        return num_play

    def update_num_wins(self,player,num_win):

        """
        if player won th match this function will add num_win by 1


        """
        if player == 1:
            num_win += 1
        elif player == 2:
            num_win += 1
        elif player == 3:
            num_win += 1
        return num_win

    def update_balance(self, a):

        """
        add or remove balance depend on the condition of each game


        """
        self.balance += int(a)
        return self.balance


def main():
    """
    main function of module player


    """
    import_class = PlayerHandler()
    my_name = import_class.read_from_file('text/account_list')
    my_balance = import_class.read_from_file('text/balance.txt')
    player1 = Player(my_name[0], int(my_balance[0]))
    player2 = Player(my_name[1], int(my_balance[1]))
    player3 = Player(my_name[2], int(my_balance[2]))
    return player1, player2, player3








