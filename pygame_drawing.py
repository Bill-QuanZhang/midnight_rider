# Pygame_Drawing
# Author: Bill
# 9 Nov 2021

# Get introduced to Pygame and draw objects on screen

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"


def main() -> None:
    """Driver of Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # Create the main loop
    while not done:
        # Make space for the event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Change the environment

        # Draw the environment
        screen.fill(WHITE)      # fill with background color
        for i in range(10):
            pygame.draw.rect(screen, RED, [100 + i * 10, 100 + i * 10, 75, 30])

        pygame.draw.circle(screen, BLUE, [500, 150], 50)

        # Update the screen
        pygame.display.flip()

        # Tick the clock
        clock.tick(60)


if __name__ == "__main__":
    main()
