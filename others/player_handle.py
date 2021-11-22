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


class PlayerHandler():
        def read_from_file(self, file_name):

            """
            read information from file

            """
            my_file = open(file_name).read().splitlines()
            return my_file

        def write_to_file(self, file_name, info1, info2, info3):

            """
            write information into file


            """

            write_my_file = open(file_name, 'w')
            write_my_file.writelines(f'{info1}\n')
            write_my_file.writelines(f'{info2}\n')
            write_my_file.writelines(f'{info3}\n')
            write_my_file.close()


