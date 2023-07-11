import sys, pygame, random
from pygame.locals import *
from ship import *

pygame.init()
screen_info = pygame.display.Info()

#1. Set up our screen - what we're going to be drawing on
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

#2. Set up a clock to control the refresh rate of our game
clock = pygame.time.Clock()
color = (3, 86, 232)

#variousables
NumLevels = 4
Level = 1
AsteroidCount = 2
#instantiate our player
player = Ship((20, 200))
AsteroidCount


def main():
    global screen
    #main game loop - this constantly updates our game
    while True:
        #controls refresh rate of our game
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:
              if event.key == K_w  :
                player.speed[1] = -5  
              if event.key == K_a:
                player.speed[0] = -5
              if event.key == K_d:
                player.speed[0] = 5
              if event.key == K_s:
                player.speed[1] = 5
                

            if event.type == KEYUP:
              if event.key == K_w:
                player.speed[1] = 0
              if event.key == K_a:
                player.speed[0] = 0
              if event.key == K_d:
                player.speed[0] = 0
              if event.key == K_s:
                player.speed[1] = 0
        player.update()
        
        #to actually make this show up
        screen.fill(color)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
       

if __name__ == '__main__':
    main()