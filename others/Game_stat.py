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


class GameStat():

    def __init__(self, game_id='_', name='_', num_plays=0, num_wins=0):
        self.__game_id = game_id
        self.__name = name
        self.__num_plays = num_plays
        self.__num_wins = num_wins

    def __str__(self):
        return f'{self.__name} #plays = {self.__num_plays}, #wins = {self.__num_wins}'

    @property
    def game_id(self):
        return self.__game_id

    @property
    def name(self):
        return self.__name

    @property
    def num_plays(self):
        return self.__num_plays

    @property
    def num_wins(self):
        return self.__num_wins

    @game_id.setter
    def game_id(self, game_id):
        self.__game_id = game_id

    @name.setter
    def name(self, name):
        self.__name = name

    @num_plays.setter
    def num_plays(self, num_plays):
        self.__num_plays = num_plays

    @num_wins.setter
    def num_wins(self, num_wins):
        self.__num_wins = num_wins


def main(player):
    import_class = PlayerHandler()
    my_play_blackjack = import_class.read_from_file('text/blackjack_play')
    my_win_blackjack = import_class.read_from_file('text/blackjack_win')

    my_play_kungfupanda = import_class.read_from_file('text/kungfupanda_play')
    my_win_kungfupanda = import_class.read_from_file('text/kungfupanda_win')

    my_play_mancala = import_class.read_from_file('text/mancala_play')
    my_win_mancala = import_class.read_from_file('text/mancala_win')

    if player == 1:
        player1_game1 = GameStat('1', 'blackjack', int(my_play_blackjack[0]) ,int(my_win_blackjack[0]))
        player1_game2 = GameStat('2', 'kungfupanda', int(my_play_kungfupanda[0]), int(my_win_kungfupanda[0]))
        player1_game3 = GameStat('3', 'mancala',int(my_play_mancala[0]) , int(my_win_mancala[0]))
        return player1_game1, player1_game2, player1_game3

    if player == 2:
        player2_game1 = GameStat('1', 'blackjack', int(my_play_blackjack[1]), int(my_win_blackjack[1]))
        player2_game2 = GameStat('2', 'kungfupanda', int(my_play_kungfupanda[1]), int(my_win_kungfupanda[1]))
        player2_game3 = GameStat('3', 'mancala', int(my_play_mancala[1]), int(my_win_mancala[1]))
        return player2_game1, player2_game2, player2_game3

    if player == 3:
        player3_game1 = GameStat('1', 'blackjack', int(my_play_blackjack[2]), int(my_win_blackjack[2]))
        player3_game2 = GameStat('2', 'kungfupanda', int(my_play_kungfupanda[2]), int(my_win_kungfupanda[2]))
        player3_game3 = GameStat('3', 'mancala', int(my_play_mancala[2]), int(my_win_mancala[2]))
        return player3_game1, player3_game2, player3_game3






