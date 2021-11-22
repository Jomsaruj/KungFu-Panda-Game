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

import pygame
import random
import Game_stat
import player
import math
import time
from player_handle import *
from pygame import mixer

player1, player2, player3 = player.main()
player1_game1, player1_game2, player1_game3 = Game_stat.main(1)
player2_game1, player2_game2, player2_game3 = Game_stat.main(2)
player3_game1, player3_game2, player3_game3 = Game_stat.main(3)


def report(a, po_score):
    """
    report score , num_play , num_win

    """

    import_class4 = player.Player()

    if po_score > 25:
        if a == 1:
            player1.balance -= 250
            player1.balance += po_score * 10
            player1_game2.num_plays = import_class4.update_num_plays(a, player1_game2.num_plays)
            player1_game2.num_wins = import_class4.update_num_wins(a, player1_game2.num_wins)

        if a == 2:
            player2.balance -= 250
            player2.balance += po_score * 10
            player2_game2.num_plays = import_class4.update_num_plays(a, player2_game2.num_plays)
            player2_game2.num_wins = import_class4.update_num_wins(a, player2_game2.num_wins)

        if a == 3:
            player3.balance -= 250
            player3.balance += po_score * 10
            player3_game2.num_plays = import_class4.update_num_plays(a, player3_game2.num_plays)
            player3_game2.num_wins = import_class4.update_num_wins(a, player3_game2.num_wins)
    else:
        if a == 1:
            player1.balance -= 250
            player1.balance += po_score * 10
            player1_game2.num_plays = import_class4.update_num_plays(a, player1_game2.num_plays)

        if a == 2:
            player2.balance -= 250
            player2.balance += po_score * 10
            player2_game2.num_plays = import_class4.update_num_plays(a, player2_game2.num_plays)

        if a == 3:
            player3.balance -= 250
            player3.balance += po_score * 10
            player3_game2.num_plays = import_class4.update_num_plays(a, player3_game2.num_plays)

    import_class5 = PlayerHandler()
    import_class5.write_to_file('text/balance.txt', player1.balance, player2.balance, player3.balance)
    import_class5.write_to_file('text/kungfupanda_play', player1_game2.num_plays, player2_game2.num_plays,player3_game2.num_plays)
    import_class5.write_to_file('text/kungfupanda_win', player1_game2.num_wins, player2_game2.num_wins,player3_game2.num_wins)


def run():

    class Po():

        def __init__(self, x=0, y=0, move_x=0):
            self.__x = x
            self.__y = y
            self.__move_x = move_x

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @property
        def move_x(self):
            return self.__move_x

        @x.setter
        def x(self, x):
            self.__x = x

        @y.setter
        def y(self, y):
            self.__y = y

        @move_x.setter
        def move_x(self, move_x):
            self.__move_x = move_x

        def show(self,po_img):
            """

            display panda

            """

            screen.blit(po_img, (self.__x, self.__y))

        def moveleft(self):

            """
            panda move to left hand side

            """
            self.__move_x = -50

        def moveright(self):

            """

            Panda move to right hand side
            """
            self.__move_x = 50

        def stop(self):
            """

            Panda stop moving
            """
            self.__move_x = 0

    class Shen():

        def __init__(self, x=0, y=0, move_y=0):
            self.__x = x
            self.__y = y
            self.__move_y = move_y

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @property
        def move_y(self):
            return self.__move_y

        @x.setter
        def x(self, x):
            self.__x = x

        @y.setter
        def y(self, y):
            self.__y = y

        @move_y.setter
        def move_y(self, move_y):
            self.__move_y = move_y

        def show(self):
            """

            display cannon
            """
            shen = pygame.image.load('Game/game3/goose.png')
            screen.blit(shen, (self.__x, self.__y))

    class Ball():

        def __init__(self, x, y, move_y):
            self.__x = x
            self.__y = y
            self.__move_y = move_y

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @property
        def move_y(self):
            return self.__move_y

        @x.setter
        def x(self, x):
            self.__x = x

        @y.setter
        def y(self, y):
            self.__y = y

        @move_y.setter
        def move_y(self, move_y):
            self.__move_y = move_y

        def show(self):
            """

            display cannon ball
            """
            ball = pygame.image.load('Game/game3/ball.png')
            screen.blit(ball, (self.__x, self.__y))


    class Text():
        def __init__(self, x, y):
            self.__x = x
            self.__y = y

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @x.setter
        def x(self, x):
            self.__x = x

        @y.setter
        def y(self, y):
            self.__y = y

        def show(self,score):
            """

            display score
            """
            font = pygame.font.Font('freesansbold.ttf', 32)
            display_po_score = font.render(f'Score : {score}', True, (255, 255, 255))
            screen.blit(display_po_score, (self.__x, self.__y))


    class Wolf():

        def __init__(self, x, y):
            self.__x = x
            self.__y = y

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @x.setter
        def x(self, x):
            self.__x = x

        @y.setter
        def y(self, y):
            self.__y = y

        def show(self):
            """

            display wolf
            """
            ball = pygame.image.load('Game/game3/wolf.png')
            screen.blit(ball, (self.__x, self.__y))

    def hitpo(po_x, po_y, ball_x, ball_y):

        """
        return true when the cannon ball hit panda


        """
        d = math.sqrt(((po_x - ball_x)**2) + ((po_y - ball_y)**2))
        if d <= 100:
            return True
        else:
            return False

    def hitshen(po_x, po_y, ball_x, ball_y):

        """
        return True if the cannon ball go back to hit cannon


        """
        d = math.sqrt(((po_x - ball_x)**2) + ((po_y - ball_y)**2))
        if d <= 10:
            return True
        else:
            return False

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    mixer.music.load('Game/game3/soundtrack.mp3')
    mixer.music.play(-1)
    pygame.display.set_caption('Kungfu panda')
    background = pygame.image.load('Game/game3/background.png')
    po_img = pygame.image.load('Game/game3/po.png')
    po = Po(350, 480, 0)
    shen1 = Shen(200, 39, 0)
    shen2 = Shen(400, 39, 0)
    shen3 = Shen(600, 39, 0)
    ball1 = Ball(200, 50, 20)
    ball2 = Ball(400, 50, 15)
    ball3 = Ball(600, 50, 10)
    wolf1 = Wolf(720, 10)
    wolf2 = Wolf(720, 90)
    wolf3 = Wolf(720, 170)
    wolf4 = Wolf(720, 250)

    display_score = Text(10, 10)

    po_score = 0
    shen_score = 0

    while True:

        screen.fill((255, 250, 250))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    po.moveleft()
                if event.key == pygame.K_RIGHT:
                    po.moveright()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    po.stop()
        po.x += po.move_x

        if po.x <= 0:
            po.x = 0
        elif po.x >= 736:
            po.x = 736

        po.show(po_img)

        shen1.show()
        shen2.show()
        shen3.show()

        ball1.y += ball1.move_y
        ball2.y += ball2.move_y
        ball3.y += ball3.move_y

        ball1.show()
        ball2.show()
        ball3.show()

        shoot_sound = mixer.Sound('Game/game3/shoot_sound.wav')
        if hitpo(po.x, po.y, ball1.x, ball1.y):
            ball1.move_y = -ball1.move_y
        if hitshen(ball1.x, ball1.y, shen1.x, shen1.y):
            ball1 = Ball(200, 50, random.randrange(18, 20))
            shoot_sound.play()
            po_score += 1

        if hitpo(po.x, po.y, ball2.x, ball2.y):
            ball2.move_y = -ball2.move_y
        if hitshen(ball2.x, ball2.y, shen2.x, shen2.y):
            ball2 = Ball(400, 50, random.randrange(14, 17))

            shoot_sound.play()
            po_score += 1

        if hitpo(po.x, po.y, ball3.x, ball3.y):
            ball3.move_y = -ball3.move_y
        if hitshen(ball3.x, ball3.y, shen3.x, shen3.y):
            ball3 = Ball(600, 50, random.randrange(10, 13))
            shoot_sound.play()
            po_score += 1

        if ball1.y > 600:
            ball1 = Ball(200, 50, 20)
            shoot_sound.play()
            shen_score += 1
            if shen_score == 4:
                break

        if ball2.y > 600:
            ball2 = Ball(400, 50, 15)
            shoot_sound.play()
            shen_score += 1
            if shen_score == 4:
                break

        if ball3.y > 600:
            ball3 = Ball(600, 50, 10)
            shoot_sound.play()
            shen_score += 1
            if shen_score == 4:
                break

        if shen_score == 1:
            wolf1.show()

        if shen_score == 2:
            wolf1.show()
            wolf2.show()

        if shen_score == 3:
            wolf1.show()
            wolf2.show()
            wolf3.show()

        if shen_score == 4:
            wolf1.show()
            wolf2.show()
            wolf3.show()
            wolf4.show()

        display_score.show(po_score)
        pygame.display.update()
    pygame.quit()
    return po_score











