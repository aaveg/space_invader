import pygame
import time
import os
from game_files.background import background
from game_files.player import player
from game_files.opponent import opponent
from game_files.functions import get_key

def main():
    pygame.init()
    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__),'data','back_music.mp3'))
    pygame.mixer.music.play(-1)
    pygame.display.set_caption('space game')
    size= (640,480)
    screen = pygame.display.set_mode(size)
    player1= player('ship.png',size)
    back= background('stars.jpg',size)
    opponents=[opponent('ship.png',size)]

    while True:
        for event in pygame.event.get():
            get_key(event,player1)

        back.draw(screen)
        for att in player1.attacks:
            att.draw(screen)
        player1.draw(screen)
        for op in opponents:
            op.draw(screen)
        pygame.display.flip()

        player1.move()
        for i in opponents:
            i.move()
        for i in player1.attacks:
            i.move(opponents)
        back.move()

        time.sleep(0.01)
        pygame.display.flip()



if __name__== '__main__' : main()
