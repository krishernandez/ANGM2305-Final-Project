import pygame
import sys
import random
import pygame.mixer

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

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

game_active = False
opponent_timer = 2000  # Slight delay
current_time = pygame.time.get_ticks()

def generate_opponents():
    x_positions = [200, 250, 300, 350, 400]
    for _ in range(6):
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
    global game_active, current_time
    pygame.mixer.init()  
    pygame.mixer.music.load('Game.mp3') 
    pygame.mixer.music.play(-1)  
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_active:
            update()
            render()
        else:
            main_menu()

        pygame.display.flip()
        clock.tick(60)

def update():
    global game_active, current_time
    handle_input()
    move_player()

    if pygame.time.get_ticks() - current_time >= opponent_timer:
        move_opponents()
        check_collision()
        scoring_system()

def Game_Over():
    screen.fill(BLACK)
    game_over_font = pygame.font.Font(None, 64)
    game_over_text = game_over_font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))

    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds before exiting the game
    pygame.quit()
    sys.exit()

def render():
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK, player_car)

    for rectangle in track_rectangles:
        rectangle.y -= 5

        if rectangle.y + rectangle.height < 0:
            rectangle.y = SCREEN_HEIGHT

        pygame.draw.rect(screen, YELLOW, rectangle)

    for opponent in opponents:
        pygame.draw.rect(screen, RED, opponent["rect"])

    score_text = score_font.render(f"Score: {score}", True, BLACK)
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
    global score, game_active

    for rectangle in track_rectangles:
        if player_car.colliderect(rectangle):
            player_car.x = player_x
            player_car.y = player_y
            score = 0
            game_active = False  # End the game on collision
            show_game_over_screen()

    for opponent in opponents:
        if player_car.colliderect(opponent["rect"]):
            player_car.x = player_x
            player_car.y = player_y
            score = 0
            game_active = False  # End the game on collision
            show_game_over_screen()

def scoring_system():
    global score, score_counter

    if score_counter % score_delay == 0:
        score += 1
    score_counter += 1
    if score_counter >= score_delay:
        score_counter = 0

def main_menu():
    global game_active, current_time
    screen.fill(BLACK)
    play_font = pygame.font.Font(None, 64)
    
    # Title
    title_font = pygame.font.Font(None, 60)
    title_text = title_font.render("A Simple Racing Game", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

    # Play Button
    play_button = pygame.Rect(200, 400, 200, 50)
    pygame.draw.rect(screen, GREEN, play_button)
    play_text = play_font.render("Play", True, BLACK)
    screen.blit(play_text, (play_button.x + play_button.width // 2 - play_text.get_width() // 2, play_button.y + play_button.height // 2 - play_text.get_height() // 2))

    # Quit Button
    quit_button = pygame.Rect(200, 500, 200, 50)
    pygame.draw.rect(screen, RED, quit_button)
    quit_text = play_font.render("Quit", True, BLACK)
    screen.blit(quit_text, (quit_button.x + quit_button.width // 2 - quit_text.get_width() // 2, quit_button.y + quit_button.height // 2 - quit_text.get_height() // 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                game_active = True
                current_time = pygame.time.get_ticks()  
            elif quit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    pygame.display.flip()

def show_game_over_screen():
    clock = pygame.time.Clock()
    game_over = True

    try_again_button = pygame.Rect(200, 600, 200, 50)

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if try_again_button.collidepoint(mouse_pos):
                    reset_game()
                    return 

        screen.fill(BLACK)
        game_over_font = pygame.font.Font(None, 64)
        game_over_text = game_over_font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))

        pygame.draw.rect(screen, GREEN, try_again_button)
        try_again_text = score_font.render("Try Again?", True, BLACK)
        screen.blit(try_again_text, (try_again_button.x + try_again_button.width // 2 - try_again_text.get_width() // 2, try_again_button.y + try_again_button.height // 2 - try_again_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

def reset_game():
    global game_active, current_time, score, opponents

    game_active = True
    current_time = pygame.time.get_ticks()
    score = 0
    opponents = []
    generate_opponents()

if __name__ == "__main__":
    main()

