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

from bj_oop import *
import Game_stat
import player
from player_handle import *

def run(a):
    end = False
    while end == False:

        bj = Blackjack()
        bj.deck = bj.initialize_cards()
        bj.shuffle_card(bj.deck)

        bj.p_hand = bj.draw_card(bj.deck, 2)
        bj.c_hand = bj.draw_card(bj.deck, 2)

        p_check = bj.validate_hand(bj.p_hand)
        c_check = bj.validate_hand(bj.c_hand)
        # ****   p_check and c_check == True is mean card is valid
        if (p_check == True) and (c_check == True):

            print("Let's play blackjack")
            print()
            print(f'Player Hand : {bj.display_cards(bj.p_hand)}')
            print(f'Computer hand : {bj.display_cards(bj.c_hand[0:1])}')

            bj.player = bj.calculate_hand_value(bj.p_hand)
            bj.computer = bj.calculate_hand_value(bj.c_hand)

            while True:

                if bj.must_draw_more(bj.computer) == True:
                    bj.c_hand = bj.c_hand + (bj.draw_card(bj.deck, 1))

                    bj.computer = bj.calculate_hand_value(bj.c_hand)

                elif bj.must_draw_more(bj.computer) == False:

                    break

            while True:

                if bj.must_draw_more(bj.player) == True:

                    print()
                    print('**** Your card is less than 16')

                    force = input('you need to draw more card. Do you want to continue(yes/no) : ').lower()  # input

                    if force == 'yes':
                        bj.p_hand = bj.p_hand+(bj.draw_card(bj.deck, 1))
                        bj.player = bj.calculate_hand_value(bj.p_hand)
                        print()
                        print(f'Your hand: {bj.display_cards(bj.p_hand)}')

                    elif force == 'no':
                        break

                elif bj.must_draw_more(bj.player) == False:

                    if bj.player < 21:
                        print()
                        option = input('More card?(yes or no) : ').lower()  # input

                        if option == 'yes':
                            bj.p_hand = bj.p_hand + bj.draw_card(bj.deck, 1)

                            bj.player = bj.calculate_hand_value(bj.p_hand)

                            print(f'Your hand: {bj.display_cards(bj.p_hand)}')
                            print(f'Computer hand: {bj.display_cards(bj.c_hand)}')

                        elif option == 'no':

                            print()
                            print(f'Computer hand: {bj.display_cards(bj.c_hand)}')
                        break
                    else:
                        print(f'Computer hand: {bj.display_cards(bj.c_hand)}')

                        break
            print()
            print('-------- Result --------')
            result_bj = bj.show_result(bj.computer, bj.player)
            print(result_bj)
            print()
            print('####################################')
            print()

            player1, player2, player3 = player.main()
            player1_game1, player1_game2, player1_game3 = Game_stat.main(1)
            player2_game1, player2_game2, player2_game3 = Game_stat.main(2)
            player3_game1, player3_game2, player3_game3 = Game_stat.main(3)

            import_class2 = player.Player()

            if result_bj == 'You win!':
                if a == 1:
                    player1.balance -= 200
                    player1_game1.num_plays = import_class2.update_num_plays(a, player1_game1.num_plays)
                    player1_game1.num_wins = import_class2.update_num_wins(a, player1_game1.num_wins)
                    player1.balance += 400

                elif a == 2:
                    player2.balance -= 200
                    player2_game1.num_plays = import_class2.update_num_plays(a, player2_game1.num_plays)
                    player2_game1.num_wins = import_class2.update_num_wins(a, player2_game1.num_wins)
                    player1.balance += 400

                elif a == 3:
                    player3.balance -= 200
                    player3_game1.num_plays = import_class2.update_num_plays(a, player3_game1.num_plays)
                    player3_game1.num_wins = import_class2.update_num_wins(a, player3_game1.num_wins)
                    player1.balance += 400

            elif result_bj == 'You tie with the computer!':
                if a == 1:
                    player1.balance -= 200
                    player1_game1.num_plays = import_class2.update_num_plays(a, player1_game1.num_plays)
                    player1.balance += 200

                elif a == 2:
                    player2.balance -= 200
                    player2_game1.num_plays = import_class2.update_num_plays(a, player2_game1.num_plays)
                    player1.balance += 200

                elif a == 3:
                    player3.balance -= 200
                    player3_game1.num_plays = import_class2.update_num_plays(a, player3_game1.num_plays)
                    player1.balance += 200

            else:
                if a == 1:
                    player1.balance -= 200
                    player1_game1.num_plays = import_class2.update_num_plays(a, player1_game1.num_plays)

                elif a == 2:
                    player2.balance -= 200
                    player2_game1.num_plays = import_class2.update_num_plays(a, player2_game1.num_plays)

                elif a == 3:
                    player3.balance -= 200
                    player3_game1.num_plays = import_class2.update_num_plays(a, player3_game1.num_plays)




            while True:
                loop = input('Play a new round: ')
                if bj.validate_input(loop) == True:
                    break

            if loop == 'no':
                print('Bye')
                end = True


        else:
            """
            This is for the case that card is invalid
            """
            print('Something went wrong , Please reset the programs')
            end = True

        import_class = PlayerHandler()
        import_class.write_to_file('text/balance.txt', player1.balance, player2.balance, player3.balance)
        import_class.write_to_file('text/blackjack_play', player1_game1.num_plays, player2_game1.num_plays, player3_game1.num_plays)
        import_class.write_to_file('text/blackjack_win', player1_game1.num_wins, player2_game1.num_wins, player3_game1.num_wins)











