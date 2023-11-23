import pygame
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

#Player car/Track, might add animated sprites if I get the time to
BLACK = (0, 0, 0)
RED = (255, 0, 0) 
GREEN = (0, 255, 0)

player_width = 30
player_height = 50
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 20  

player_car = pygame.Rect(player_x, player_y, player_width, player_height)

track_rectangles = [
    pygame.Rect(100, 100, 20, 50),
    pygame.Rect(100, 200, 20, 50),
    pygame.Rect(100, 300, 20, 50),
    pygame.Rect(100, 400, 20, 50),
    pygame.Rect(100, 500, 20, 50),
    pygame.Rect(100, 600, 20, 50),
    pygame.Rect(100, 700, 20, 50),
    pygame.Rect(100, 800, 20, 50),
    pygame.Rect(100, 900, 20, 50),
    pygame.Rect(100, 1000, 20, 50),
    pygame.Rect(500, 100, 20, 50),
    pygame.Rect(500, 200, 20, 50),
    pygame.Rect(500, 300, 20, 50),
    pygame.Rect(500, 400, 20, 50),
    pygame.Rect(500, 500, 20, 50),
    pygame.Rect(500, 600, 20, 50),
    pygame.Rect(500, 700, 20, 50),
    pygame.Rect(500, 800, 20, 50),
    pygame.Rect(500, 900, 20, 50),
    pygame.Rect(500, 1000, 20, 50),  
]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("A Simple Racing Game")

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        update()
        render()

        pygame.display.flip()
        clock.tick(60) 

def update():
    handle_input()
    move_player()

def render():
    screen.fill(BLACK) 
    pygame.draw.rect(screen, RED, player_car)

    for rectangle in track_rectangles:
        rectangle.y -= 5

        if rectangle.y + rectangle.height < 0:
            rectangle.y = SCREEN_HEIGHT

        pygame.draw.rect(screen, GREEN, rectangle)

def handle_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_car.x -= 5
    if keys[pygame.K_RIGHT]:
        player_car.x += 5
    if keys[pygame.K_UP]:
       player_car.y -= 5 
    if keys[pygame.K_DOWN]:
        player_car.y += 5

#These aren't really in order, I need to figure out what order these go in the code...

#TODO: Add collision detection to make sure car does not go out of bounds
#TODO: Add collision to race track, this will confine the car to the track only
def move_player():
    pass

#TODO: Add basic AI for opposing cars/obstacles in the track
def enemy_input():
    pass

#TODO: Simple scoring system: the longer you last, the more points you earn
def scoring_system():
    pass

#TODO: Simple menu with play and quit button
def main_menu():
    pass

if __name__ == "__main__":
    main()
