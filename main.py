# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from shot import *
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #bundeling stuff up
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroidField = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    #clock for determining the fps of the game
    dt = 0
    clock = pygame.time.Clock()
    
    #player
    objPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)

    #asteroid field
    objAsteroidfield = AsteroidField()

    #gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))#clear screen

        updatable.update(dt)

        #check for player colissions
        for asteroid_object in asteroid:
            if objPlayer.collision(asteroid_object):
                print("Game over!")
                sys.exit()
        #check for shot collisions
        for asteroid_object in asteroid:
            for shot in shots:
                if (shot.position.x < 0 or shot.position.x > SCREEN_WIDTH or shot.position.y < 0 or shot.position.y > SCREEN_HEIGHT):
                    shot.kill()
                elif asteroid_object.collision(shot):
                    asteroid_object.kill()
                    shot.kill()

        for unit in drawable:
            unit.draw(screen) #draw onto screen
        pygame.display.flip()
        dt = clock.tick(60)/1000 #sets 60 fps and outputs it to dt converted to seconds
        print(f"{dt}", end="\r")
 
        


if __name__== "__main__":
    main()