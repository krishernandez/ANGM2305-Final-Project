import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0)
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

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

opponents = []
score = 0
score_delay = 10  
score_counter = 0
score_font = pygame.font.Font(None, 36)

def generate_opponents():
    x_positions = [100, 200, 300, 400, 500]  # Adjust these as needed
    for _ in range(5):  # Adjust the number of opponents
        x = random.choice(x_positions)
        y = random.randint(-300, -50)  
        width = random.randint(20, 50)  
        height = random.randint(40, 80)  
        speed = random.randint(3, 8)  

        opponent = pygame.Rect(x, y, width, height)
        opponents.append({"rect": opponent, "speed": speed})

generate_opponents()

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
    move_opponents()
    check_collision()
    scoring_system()

def render():
    screen.fill(BLACK) 
    pygame.draw.rect(screen, RED, player_car)

    for rectangle in track_rectangles:
        rectangle.y -= 5

        if rectangle.y + rectangle.height < 0:
            rectangle.y = SCREEN_HEIGHT

        pygame.draw.rect(screen, GREEN, rectangle)

    for opponent in opponents:
        pygame.draw.rect(screen, WHITE, opponent["rect"])

    score_text = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

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
    player_car.x = max(0, min(player_car.x, SCREEN_WIDTH - player_car.width))
    player_car.y = max(0, min(player_car.y, SCREEN_HEIGHT - player_car.height))

def move_opponents():
    for opponent in opponents:
        opponent["rect"].y += opponent["speed"]

        if opponent["rect"].y > SCREEN_HEIGHT:
            opponent["rect"].y = random.randint(-300, -50)  
            opponent["rect"].x = random.choice([200, 250, 300, 350, 400])
            opponent["rect"].width = random.randint(20, 50)
            opponent["rect"].height = random.randint(40, 80)
            opponent["speed"] = random.randint(3, 8)

def check_collision():
    global score  

    for rectangle in track_rectangles:
        if player_car.colliderect(rectangle):
            player_car.x = player_x
            player_car.y = player_y
            score = 0  

    for opponent in opponents:
        if player_car.colliderect(opponent["rect"]):
            player_car.x = player_x
            player_car.y = player_y
            score = 0  

def scoring_system():
    global score, score_counter

    if score_counter % score_delay == 0:
        score += 1
    score_counter += 1
    if score_counter >= score_delay:
        score_counter = 0

#TODO: Simple menu with play and quit button
def main_menu():
    pass

#TODO: Game Over screen and Try Again button

if __name__ == "__main__":
    main()



