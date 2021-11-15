# Pygame Boilerplate
# Author: Bill
# 2021 Version


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
WINDOW_TITLE = "<<Your Title Here>>"


class Dvdimage:
    """Represents a dvdimage on screen

    Attributes:
        x, y: coordinates of top-left corner
        width: width of our rectangle in px
        height: height of our rectangle in ps
        colour: 3-tuple of (r, g, b)
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 150
        self.height = 90
        self.colour = RED

    def rect(self) -> pygame.rect:
        """Return a pygame.rect that represents the dvd_image"""
        return [self.x, self.y, self.width, self.height]


def main() -> None:
    """Driver of Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()

    # Create the main loop
    while not done:
        # Make space for the event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Change the environment

        # Draw the environment
        screen.fill(WHITE)      # fill with background color
        # for i in range(10):
        #     pygame.draw.rect(screen, RED, [100 + i * 10, 100 + i * 10, 75, 30])

        # pygame.draw.circle(screen, BLUE, [500, 150], 50)

        # Draw our Dvdimage
        pygame.draw.rect(screen, dvd_image.colour, dvd_image.rect())  # method

        # Update the screen
        pygame.display.flip()

        # Tick the clock
        clock.tick(60)


if __name__ == "__main__":
    main()
