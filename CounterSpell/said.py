import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Level Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.SysFont("Arial", 36)

# Game state
LEVEL_1, LEVEL_2, LEVEL_3, VICTORY, FAILURE = 1, 2, 3, 4, 5
current_level = LEVEL_1
score = 0
target_scores = {LEVEL_1: 50, LEVEL_2: 100}
clock = pygame.time.Clock()


def draw_text(text, x, y, color=WHITE):
    """Utility function to render text on the screen."""
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def display_instructions(message):
    """Displays instructions for 10 seconds."""
    screen.fill(BLACK)
    draw_text(message, WIDTH // 2 - 200, HEIGHT // 2 - 50, WHITE)
    pygame.display.flip()
    time.sleep(10)


def pacman_level():
    """Logic for Pac-Man-like gameplay."""
    global score, current_level
    player = pygame.Rect(100, 100, 50, 50)
    enemies = [pygame.Rect(200, 200, 50, 50), pygame.Rect(400, 400, 50, 50)]
    running = True
    score = 0

    while running:
        screen.fill(BLACK)
        draw_text(f"Level 1: Pac-Man | Score: {score}", 20, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.y -= 5
        if keys[pygame.K_DOWN]:
            player.y += 5
        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5

        pygame.draw.rect(screen, BLUE, player)
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)

        # Simulate scoring
        score += 1
        if score >= target_scores[LEVEL_1]:
            current_level = LEVEL_2
            running = False
        elif score > 0 and score % 300 == 0:
            draw_text("You failed!", WIDTH // 2 - 100, HEIGHT // 2, RED)
            pygame.display.flip()
            time.sleep(2)
            current_level = FAILURE
            running = False

        pygame.display.flip()
        clock.tick(30)


def flappy_bird_level():
    """Logic for Flappy Bird-like gameplay."""
    global score, current_level
    bird = pygame.Rect(100, HEIGHT // 2, 50, 50)
    gravity = 2
    velocity = 0
    pipes = [pygame.Rect(WIDTH, HEIGHT // 2 - 150, 100, 300)]
    running = True
    score = 0

    while running:
        screen.fill(BLACK)
        draw_text(f"Level 2: Flappy Bird | Score: {score}", 20, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                velocity = -10

        # Bird movement
        velocity += gravity
        bird.y += velocity

        # Pipe movement
        for pipe in pipes:
            pipe.x -= 5
            if pipe.x + pipe.width < 0:
                pipes.remove(pipe)
                pipes.append(pygame.Rect(WIDTH, HEIGHT // 2 - 150, 100, 300))
                score += 1

        # Check for score threshold
        if score >= target_scores[LEVEL_2]:
            current_level = LEVEL_3
            running = False
        elif score > 0 and score % 300 == 0:
            draw_text("You failed!", WIDTH // 2 - 100, HEIGHT // 2, RED)
            pygame.display.flip()
            time.sleep(2)
            current_level = FAILURE
            running = False

        # Draw elements
        pygame.draw.rect(screen, GREEN, bird)
        for pipe in pipes:
            pygame.draw.rect(screen, RED, pipe)

        pygame.display.flip()
        clock.tick(30)


def victory_screen():
    """Victory screen."""
    screen.fill(BLACK)
    draw_text("You Win!", WIDTH // 2 - 100, HEIGHT // 2, GREEN)
    draw_text("Press Q to Quit", WIDTH // 2 - 100, HEIGHT // 2 + 50, GREEN)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_q
            ):
                pygame.quit()
                sys.exit()


def failure_screen():
    """Failure screen."""
    screen.fill(BLACK)
    draw_text("You Failed!", WIDTH // 2 - 100, HEIGHT // 2, RED)
    draw_text("Press Q to Quit", WIDTH // 2 - 100, HEIGHT // 2 + 50, RED)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_q
            ):
                pygame.quit()
                sys.exit()


# Main Game Loop
while True:
    if current_level == LEVEL_1:
        display_instructions("Level 1: Pac-Man - Score at least 50 to advance!")
        pacman_level()
    elif current_level == LEVEL_2:
        display_instructions("Level 2: Flappy Bird - Score at least 100 to advance!")
        flappy_bird_level()
    elif current_level == LEVEL_3:
        display_instructions("Level 3: Tetris - TBD!")
        # Call tetris_level()
    elif current_level == VICTORY:
        victory_screen()
    elif current_level == FAILURE:
        failure_screen()