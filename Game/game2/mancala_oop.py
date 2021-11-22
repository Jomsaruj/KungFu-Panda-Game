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
from player_handle import *


def run(a):

    class Board():
        def __init__(self, board=[], player=0, com=0, game_over='_',winner='_'):
            self.__board = board
            self.__player = player
            self.__com = com
            self.__game_over = game_over
            self.__winner = winner

        @property
        def board(self):
            return self.__board

        @property
        def player(self):
            return self.__player

        @property
        def com(self):
            return self.__com

        @property
        def game_over(self):
            return self.__game_over

        @property
        def winner(self):
            return self.__winner


        @board.setter
        def board(self, board):
            self.__board = board

        @player.setter
        def player(self, player):
            self.__player = player

        @com.setter
        def com(self, com):
            self.__com = com

        @game_over.setter
        def game_over(self, game_over):
            self.__game_over = game_over

        @winner.setter
        def winner(self, winner):
            self.__winner = winner

        def create(self):
            """
            create the board or the list with 14 nested list inside


            """

            self.board = []
            for index in range(14):
                self.board.append([])
            for player in range(6):
                self.board[player].append(4)
            for com in range(7, 13):
                self.board[com].append(4)
            self.board[13].append(0)
            self.board[6].append(0)

        def show_board(self):
            """
            show the board that already generated


            """
            print(f'-'*30)
            print(f'           {self.board[13]}           ')

            print(f'  (1)| {self.board[0]}     {self.board[12]} |(13)  ')
            print(f'  (2)| {self.board[1]}     {self.board[11]} |(12)  ')
            print(f'  (3)| {self.board[2]}     {self.board[10]} |(11)  ')
            print(f'  (4)| {self.board[3]}     {self.board[9]} |(10)  ')
            print(f'  (5)| {self.board[4]}     {self.board[8]} |(9)  ')
            print(f'  (6)| {self.board[5]}     {self.board[7]} |(8)  ')

            print(f'           {self.board[6]}           ')
            print(f'-' * 30)

        def game(self):
            """
            return done when game is over , return Continue when the game is not over


            """
            count = 0
            for i in range(0, 6):
                if self.board[i][0] == 0 or self.board[i][0] == 1:
                    count += 1
            for j in range(7, 13):
                if self.board[j][0] == 0 or self.board[j][0] == 1:
                    count += 1
            if count == 12:
                self.game_over = 'done'
            else:
                self.game_over = 'continue'

        def input_decision(self):
            """

            Enter player move
            """

            while True:
                choice = int(input('Which slot (1,2,3,4,5) : '))
                if choice > 6 and choice <= 14:
                    print("You can't choose this slot!!")
                elif choice > 14:
                    print(f"There is no {choice} slot!!")
                elif my_board.board[choice-1][0] == 0:
                    print(f'Empty space !')

                elif self.board[choice - 1][0] == 1:
                    if choice == 6:
                        self.board[6][0] += 1
                        self.board[5] = [0]
                        self.show_board()
                        self.show_current_score()
                        self.input_decision()
                        self.walk_player()
                        break

                    elif self.board[choice][0] == 0:

                        self.board[choice - 1] = [0]
                        self.board[choice][0] += 1
                        self.show_board()
                        self.show_current_score()
                        self.player = choice
                        break

                    else:

                        self.board[choice - 1] = [0]
                        self.board[choice][0] += 1
                        self.show_board()
                        self.show_current_score()
                        self.player = choice
                        self.walk_player()
                        break
                else:
                    self.player = choice-1
                    break

        def for_developer_check(self):
            """

            Enter Computer move
            """
            while True:
                choice = int(input('Enter Computer option (for checking my work) : '))

                if choice < 8 or choice > 13:
                    print('Invalid option !')

                elif my_board.board[choice-1][0] == 0:
                    print(f'Empty space !')

                elif self.board[choice - 1][0] == 1:
                    if choice == 13:
                        self.board[13][0] += 1
                        self.board[12] = [0]
                        self.show_board()
                        self.show_current_score()
                        self.for_developer_check()
                        self.walk_com()
                        break

                    elif self.board[choice][0] == 0:

                        self.board[choice - 1] = [0]
                        self.board[choice][0] += 1
                        self.show_board()
                        self.show_current_score()
                        self.com = choice
                        break

                    else:

                        self.board[choice - 1] = [0]
                        self.board[choice][0] += 1
                        self.show_board()
                        self.show_current_score()
                        self.com = choice
                        self.walk_com()
                        break

                else:
                    self.com = choice - 1
                    break

        def show_current_score(self):
            """
            print index 6 which is player pocket and index 13 which is computer pocket


            """
            print('Current score')
            print(f'Player : {self.board[6][0]}')
            print(f'Com : {self.board[13][0]}')

        def walk_player(self):
            """

            generate player move
            """
            while self.board[self.player][0] - 1 != 0:
                start = self.player + 1
                stop = self.player + self.board[self.player][0]
                if stop > 13:
                    new_stop = 12
                    for i in range(start, new_stop+1):
                        self.board[i][0] += 1
                    self.board[self.player] = [0]
                    excess = stop - 13
                    if excess == 1:
                        self.board[0][0] += 1
                        self.player = excess-1
                        self.show_board()
                        self.show_current_score()
                        self.walk_player()

                    else:
                        for j in range(excess+1):
                            self.board[j][0] += 1

                        self.show_board()
                        self.show_current_score()
                        self.player = excess
                        self.walk_player()

                elif stop == 13:
                    new_stop = 12
                    for i in range(start, new_stop + 1):
                        self.board[i][0] += 1
                    self.board[self.player] = [0]
                    self.board[0][0] += 1
                    self.show_board()
                    self.show_current_score()
                    self.player = 0
                    self.walk_player()

                elif stop == 6:

                    for i in range(start, stop + 1):
                        self.board[i][0] += 1
                    self.board[self.player] = [0]
                    self.show_board()
                    self.show_current_score()
                    self.input_decision()
                    self.walk_player()
                else:

                    for i in range(start, stop+1):
                        self.board[i][0] += 1
                    self.board[self.player] = [0]
                    self.player = stop
                    self.show_board()
                    self.show_current_score()

        def walk_com(self):
            """

            generate computer move
            """
            while self.board[self.com][0] - 1 != 0:
                start = self.com + 1
                stop = self.com + self.board[self.com][0]

                if stop > 13: # perfect
                    new_stop = 13
                    for i in range(start, new_stop+1):
                        self.board[i][0] += 1
                    self.board[self.com] = [0]
                    excess = stop - 13
                    if excess == 1:
                        self.board[0][0] += 1
                        self.com = 0
                        self.show_board()
                        self.show_current_score()
                        self.walk_com()
                    elif excess == 6:
                        self.board[7][0] += 1
                        self.show_board()
                        self.show_current_score()
                        self.com = 7
                        self.walk_com()
                    elif excess > 6:
                        for j in range(excess+2):
                            self.board[j][0] += 1
                        self.board[6][0] -= 1
                        self.show_board()
                        self.show_current_score()
                        self.com = excess
                        self.walk_com()

                    else:
                        for j in range(excess):
                            self.board[j][0] += 1

                        self.show_board()
                        self.show_current_score()
                        self.com = excess-1
                        self.walk_com()
                elif stop == 13:
                    for i in range(start, stop + 1):
                        self.board[i][0] += 1
                    self.board[self.com] = [0]
                    self.show_board()
                    self.show_current_score()
                    self.for_developer_check()
                    self.walk_com()

                else:
                    if stop == 6:
                        a = self.com + 1
                        while a <= 5:
                            self.board[a][0] += 1
                            a += 1

                        self.board[self.com] = [0]
                        self.board[7][0] += 1
                        self.show_board()
                        self.show_current_score()
                        self.com = 7
                        self.walk_com()
                    elif start < 6 and stop > 6:
                        self.board[self.com] = [0]
                        for i in range(start, stop + 2):
                            self.board[i][0] += 1
                        self.board[6][0] -= 1
                        self.show_board()
                        self.show_current_score()
                        self.com = stop+1
                        self.walk_com()
                    else:

                        for i in range(start, stop+1):
                            self.board[i][0] += 1
                        self.board[self.com] = [0]
                        self.com = stop
                        self.show_board()
                        self.show_current_score()

        def show_result(self):
            """

            show self.winner
            """
            player = self.board[6][0]
            com = self.board[13][0]
            if player > com:
                self.winner = 'player'
            elif com > player:
                self.winner = 'com'
            else:
                self.winner = 'drew'
            print()
            print(f'Result')
            print(f'Player : {player}')
            print(f'Com    : {com}')
            print(f'The winner is : {self.winner}')


    my_board = Board()


    my_board.create()
    print("Let's play Mancala !!")
    my_board.show_board()
    while True:
        my_board.game()

        my_board.input_decision()
        my_board.walk_player()
        if my_board.game_over == 'done':
            break
        elif my_board.game_over == 'continue':
            print()
            my_board.for_developer_check()
            my_board.walk_com()
            my_board.game()
            if my_board.game_over == 'done':
                break
    my_board.show_result()

    import_class4 = player.Player()

    player1, player2, player3 = player.main()
    player1_game1, player1_game2, player1_game3 = Game_stat.main(1)
    player2_game1, player2_game2, player2_game3 = Game_stat.main(2)
    player3_game1, player3_game2, player3_game3 = Game_stat.main(3)

    if my_board.winner == 'player':
        if a == 1:
            player1.balance -= 200
            player1.balance += 400
            player1_game2.num_plays = import_class4.update_num_plays(a, player1_game3.num_plays)
            player1_game2.num_wins = import_class4.update_num_wins(a, player1_game3.num_wins)

        if a == 2:
            player2.balance -= 200
            player2.balance += 400
            player2_game2.num_plays = import_class4.update_num_plays(a, player2_game3.num_plays)
            player2_game2.num_wins = import_class4.update_num_wins(a, player2_game3.num_wins)

        if a == 3:
            player3.balance -= 200
            player3.balance += 400
            player3_game2.num_plays = import_class4.update_num_plays(a, player3_game3.num_plays)
            player3_game2.num_wins = import_class4.update_num_wins(a, player3_game3.num_wins)
    else:
        if a == 1:
            player1.balance -= 200

            player1_game2.num_plays = import_class4.update_num_plays(a, player1_game3.num_plays)

        if a == 2:
            player2.balance -= 200

            player2_game2.num_plays = import_class4.update_num_plays(a, player2_game3.num_plays)

        if a == 3:
            player3.balance -= 200

            player3_game2.num_plays = import_class4.update_num_plays(a, player3_game3.num_plays)

    import_class_for_mancala = PlayerHandler()
    import_class_for_mancala.write_to_file('text/balance.txt', player1.balance, player2.balance, player3.balance)
    import_class_for_mancala.write_to_file('text/mancala_play', player1_game2.num_plays, player2_game2.num_plays,player3_game2.num_plays)
    import_class_for_mancala.write_to_file('text/mancala_win', player1_game2.num_wins, player2_game2.num_wins,player3_game2.num_wins)
