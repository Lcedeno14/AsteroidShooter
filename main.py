import pygame
from constants import * 
from player import Player
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        #limit game fps to 60
        dt = clock.tick(60) /1000
        
if __name__ == "__main__":
    main()

# import pygame
# from constants import *
# from player import Player


# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     clock = pygame.time.Clock()
#     player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     dt = 0

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return

#         player.update(dt)

#         screen.fill("black")
#         player.draw(screen)
#         pygame.display.flip()

#         # limit the framerate to 60 FPS
#         dt = clock.tick(60) / 1000


# if __name__ == "__main__":
#     main()
