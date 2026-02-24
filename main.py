import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock_obj = pygame.time.Clock()
    dt = 0

    #Inifinite Loop!
    while(True):
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass

        screen.fill("black")

        #Refresh the screen - last!
        pygame.display.flip()

        #Clock obj will pause 1/60 per loop; returns time in ms (/1000 = sec)
        dt = clock_obj.tick(60) / 1000
        #print(f"dt: {dt}") #see that it's working and generally stable


if __name__ == "__main__":
    main()
