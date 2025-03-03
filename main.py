# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    #clock for determining the fps of the game
    dt = 0
    clock = pygame.time.Clock()
    
    #player
    objPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)

    #gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        objPlayer.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000 #sets 60 fps and outputs it to dt converted to seconds
        print(f"{dt}", end="\r")
 
        


if __name__== "__main__":
    main()