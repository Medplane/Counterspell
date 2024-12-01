import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite 1 Story")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Font setup
font = pygame.font.Font(None, 36)

# Text lines for the story
lines = [
    "I want to quit gaming.",
    "It's been too much to handle.",
    "Maybe there's more out there for me.",
    "I can't keep running from reality.",
    "Fainted... into another world."
]

# Function to display text
def display_text(text, y_offset):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Function to display transition screen
def show_transition(messages, duration=3000):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < duration:
        screen.fill(black)
        for idx, message in enumerate(messages):
            display_text(message, idx * 50 - 50)  # Offset each line by 50px
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Display the initial story
current_line = 0
line_timer = 0
line_delay = 2000  # Delay in milliseconds between lines
fade_out = False
sprite_alpha = 255
fade_speed = 5

# Main loop to show the initial story
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black color
    screen.fill(black)

    # Show the lines one by one
    if current_line < len(lines):
        display_text(lines[current_line], 0)
        line_timer += clock.get_time()
        if line_timer >= line_delay:
            line_timer = 0
            current_line += 1
    else:
        # Transition to the next phase (fading out)
        fade_out = True

    if fade_out:
        sprite_alpha -= fade_speed
        if sprite_alpha < 0:
            sprite_alpha = 0
            fade_out = False
            break  # Break the loop once the fade is complete

        fade_surface = pygame.Surface((screen_width, screen_height))
        fade_surface.fill(black)
        fade_surface.set_alpha(255 - sprite_alpha)
        screen.blit(fade_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

# Import and play Pacman
folder_a_path = r'./Pacman-master'
if folder_a_path not in sys.path:
    sys.path.append(folder_a_path)

import pacman
from pacman import game_won as pacman_won

pacman.main()  # Run Pacman game
if pacman_won:  # Check if Pacman was won
    show_transition(["Impossible", "You won't get away in the next game."])

# Import and play Tetris
def show_transition(messages):
    for message in messages:
        print(message)  # Display transition messages

# Import and play Tetris
#If You Want to skip Pacman and try the rest get rid of the comment in next line
#pacman_won=True
import sys
import pygame
if pacman_won:
    tetris_path = r'./New_Tetris'
    if tetris_path not in sys.path:
        sys.path.append(tetris_path)


    import tetris
    from tetris import tetris_game_over
    # Run Tetris game
    if tetris_game_over:  # Check if Tetris was won
        show_transition(["Fool! You won't escape.", "The next game will destroy you."])

    # Reinitialize pygame for the next game
    pygame.quit()
    pygame.init()

# Import and play Flappy Bird
#If You Want to skip Tetris and try the rest get rid of the comment in next line
#tetris_game_over=True
import sys
import pygame
tetris_game_over=True
if tetris_game_over:
    flappy_bird_path = r'./flappy-bird-main'
    if flappy_bird_path not in sys.path:
        sys.path.append(flappy_bird_path)

    import flappy_bird
    from flappy_bird import game_won as flappy_bird_won

    flappy_bird.main()  # Run Flappy Bird game
    if flappy_bird_won:  # Check if Flappy Bird was won
        show_transition(["I can't believe it!", "You are worthy to leave."])

# Quit pygame
pygame.quit()
sys.exit()