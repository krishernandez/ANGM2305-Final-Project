import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_car = pygame.Rect(50, 50, 30, 50)

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
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player_car)

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

def move_player():
    pass

if __name__ == "__main__":
    main()
