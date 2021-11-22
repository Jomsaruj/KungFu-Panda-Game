import error_oop


class Blackjack():

    def __init__(self, player='0', computer='0', deck='_' , p_hand='_' , c_hand='_'):
        self.__player = player
        self.__computer = computer
        self.__deck = deck
        self.__p_hand = p_hand
        self.__c_hand = c_hand

    @property
    def player(self):
        return self.__player

    @property
    def computer(self):
        return self.__computer

    @property
    def deck(self):
        return self.__deck

    @property
    def p_hand(self):
        return self.__p_hand

    @property
    def c_hand(self):
        return self.__c_hand

    @player.setter
    def player(self, player):
        self.__player = player

    @computer.setter
    def computer(self, computer):
        self.__computer = computer

    @deck.setter
    def deck(self,deck):
        self.__deck = deck

    @p_hand.setter
    def p_hand(self,p_hand):
        self.__p_hand = p_hand

    @c_hand.setter
    def c_hand(self,c_hand):
        self.__c_hand = c_hand

    def initialize_cards(self):

        """
        This function will generate the deck of the card.

        """
        SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = []
        for rank in RANKS:
            for suit in SUITS:
                card = rank + ' ' + suit
                deck += [card]
        return deck

    def shuffle_card(self, deck):

        """
        This function will shuffle the deck that generate from function initialize_card

        """
        import random
        n = len(deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = deck[r]
            deck[r] = deck[i]
            deck[i] = temp

    def display_cards(self,lcards):

        """
        This function will convert the card from ['2 Hearts'] to 2♥
        >>> display_cards(['2 Hearts'])
        '2♥ '
        >>> display_cards(['3 Hearts'])
        '3♥ '
        >>> display_cards(['2 Clubs'])
        '2♣ '
        >>> display_cards(['2 Diamonds'])
        '2♦ '
        >>> display_cards(['2 Spades'])
        '2♠ '
        >>> display_cards(['Ace Hearts'])
        'Ace♥ '


        """

        display_str = ""
        for each_card in lcards:
            ltemp = each_card.split()
            if ltemp[1] == 'Clubs':
                display_str += ltemp[0] + '\u2663' + ' '
            elif ltemp[1] == 'Diamonds':
                display_str += ltemp[0] + '\u2666' + ' '
            elif ltemp[1] == 'Hearts':
                display_str += ltemp[0] + '\u2665' + ' '

            else:
                display_str += ltemp[0] + '\u2660' + ' '

        return display_str

    def draw_card(self, deck, n):

        """Pick the top card (index[0])from the deck"""
        get_list = []
        for i in range(n):
            get_list.append(deck[i])
            deck.remove(deck[i])
        return get_list

    def calculate_hand_value(self, hand):
        """
        Calculate the total value of your hand

        >>> calculate_hand_value(['2 Clubs', 'Ace Spades', 'Ace Clubs', '4 Clubs'])
        18
        >>> calculate_hand_value(['Ace Diamonds', '8 Clubs'])
        19
        >>> calculate_hand_value(['Ace Diamonds', '8 Clubs', '7 Clubs'])
        16
        >>> calculate_hand_value(['Ace Hearts', 'Ace Diamonds'])
        12
        >>> calculate_hand_value(['Ace Hearts', 'Ace Diamonds', '2 Clubs', '10 Diamonds']) # problem
        14
        >>> calculate_hand_value(['Jack Clubs', '7 Hearts', 'Queen Hearts'])
        27
        >>> calculate_hand_value(['King Hearts', 'Queen Clubs'])
        20
        >>> calculate_hand_value(['Ace Spades', 'Queen Spades'])
        21
        >>> calculate_hand_value(['4 Hearts', '9 Hearts', '4 Diamonds'])
        17
        >>> calculate_hand_value(['4 Hearts', '9 Hearts', '4 Diamonds', '8 Spades'])
        25
        >>> calculate_hand_value(['4 Hearts', '9 Hearts', 'Ace Diamonds', '7 Spades'])
        21
        >>> calculate_hand_value(['2 Hearts', 'Ace Hearts', '9 Diamonds', '6 Spades' , '4 Hearts'])
        22
        """
        value_list = []
        for each_card in hand:
            card_value = each_card.split()

            if card_value[0] == 'Jack' or card_value[0] == 'Queen' or card_value[0] == 'King':
                value = 10
            elif card_value[0] == 'Ace':

                value = 11

            else:
                value = card_value[0]
            value_list.append(int(value))

        total_hand = sum(value_list)
        #######################################
        if 11 in value_list and total_hand > 21:
            a = 1
            num_ace = value_list.count(11)
            while a <= num_ace:
                if total_hand <= 21:
                    pass

                elif total_hand > 21:
                    value_list.remove(11)
                    value_list.append(1)
                    total_hand = sum(value_list)
                a += 1

        total_hand = sum(value_list)
        return total_hand

    def must_draw_more(self, hand):
        """

        return True if hand value < 16 , return False if hand >= 16

        >>> must_draw_more(9)
        True
        >>> must_draw_more(14)
        True
        >>> must_draw_more(20)
        False
        >>> must_draw_more(2)
        True
        >>> must_draw_more(16)
        False
        >>> must_draw_more(15)
        True

        """
        if hand >= 16:
            return False
        else:
            return True

    def show_result(self,com_hand, p_hand):
        """
        return the result of the game

        >>> show_result(21, 21)
        Computer hand : 21
        Player hand   : 21
        You tie with the computer!

        >>> show_result(18, 18)
        Computer hand : 18
        Player hand   : 18
        You tie with the computer!

        >>> show_result(21, 20)
        Computer hand : 21
        Player hand   : 20
        You loose!

        >>> show_result(20, 21)
        Computer hand : 20
        Player hand   : 21
        You win!

        >>> show_result(18, 15)
        Computer hand : 18
        Player hand   : 15
        You lose because your card is less than 16.

        >>> show_result(29, 22)
        Computer hand : 29
        Player hand   : 22
        You tie with the computer!



        """
        print(f'Computer hand : {com_hand}')
        print(f'Player hand   : {p_hand}')
        if p_hand > 21:
            if com_hand > 21:
                return 'You tie with the computer!'
            elif com_hand <= 21:
                return 'You loose!'
        elif p_hand < 16:
            if com_hand > 21:
                return 'You tie with the computer!'
            else:
                return 'You lose because your card is less than 16.'
        elif p_hand < 21:
            if com_hand > 21:
                return 'You win!'
            elif com_hand == p_hand:
                return 'You tie with the computer!'
            elif com_hand <= 21:
                if p_hand > com_hand:
                    return 'You win!'
                else:
                    return 'You loose!'
        elif p_hand == 21:
            if com_hand == 21:
                return 'You tie with the computer!'
            else:
                return 'You win!'

    def validate_hand(self,lcard):
        """If card is invalid return False(card invalid when number is not in rank or type is not in suit)

        >>> validate_hand(['21 Clubs'])
        Found this invalid rank 21 ; rank must be in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        False

        >>> validate_hand(['1 Clubs'])
        Found this invalid rank 1 ; rank must be in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        False

        >>> validate_hand(['2 Club'])
        Found this invalid suit Club ; suite must be in ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        False

        >>> validate_hand(['2 pie'])
        Found this invalid suit pie ; suite must be in ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        False

        >>> validate_hand(['2 Clubs'])
        True
        """
        suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for each_card in lcard:
            ltemp = each_card.split()
            try:
                if ltemp[0] not in rank:
                    raise error_oop.InvalidCardRank
                if ltemp[1] not in suit:
                    raise error_oop.InvalidCardSuit

            except error_oop.InvalidCardRank:
                print("Found this invalid rank", ltemp[0], "; rank must be in", rank)
                return False
            except error_oop.InvalidCardSuit:
                print("Found this invalid suit", ltemp[1], "; suite must be in", suit)
                return False
        return True

    def validate_input(self,option):
        """
        return False if option not = yes or no

        >>> validate_input('yes')
        True

        >>> validate_input('ye')
        <BLANKLINE>
        You must enter only yes or no. Please enter again
        False

        >>> validate_input('no')
        True

        >>> validate_input('yep')
        <BLANKLINE>
        You must enter only yes or no. Please enter again
        False

        >>> validate_input('sad')
        <BLANKLINE>
        You must enter only yes or no. Please enter again
        False

        """
        try:
            if option != 'yes' and option != 'no':
                raise error_oop.InvalidInput
        except error_oop.InvalidInput:
            print()
            print('You must enter only yes or no. Please enter again')
            return False
        return True
