import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock_obj = pygame.time.Clock()
    dt = 0

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Adding the Player class to the groups before the player obj instance is created
    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, drawable, updatable)

    #Instantiate a Player object
    player_one = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()

    #Inifinite Loop!
    while(True):
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass

        screen.fill("black")

        #Clock obj will pause 1/60 per loop; returns time in ms (/1000 = sec)
        dt = clock_obj.tick(60) / 1000
        #print(f"dt: {dt}") #see that it's working and generally stable

        #Update the player's state before rendering...
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collideswith(player_one):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collideswith(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()
                    

        #Draw the player to the screen after it's filled with black, but before it's flipped!
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        #Refresh the screen - last!
        pygame.display.flip()

        


if __name__ == "__main__":
    main()
