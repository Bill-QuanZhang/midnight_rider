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
        width: width of image in px
        height: height of image in ps
        # colour: 3-tuple of (r, g, b)
        img: visual representation of our dvdimage
        x-vel: x velocity in px/second
        y-vel: y velocity in px/second
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 400
        self.height = 497
        # self.colour = RED
        self.img = pygame.image.load("./images/163600626.jpeg")
        self.x_vel = 5
        self.y_vel = 3

    def rect(self) -> pygame.rect:
        """Return a pygame.rect that represents the dvd_image"""
        return [self.x, self.y, self.width, self.height]

    def update(self) -> None:
        """Update the dvdimage with x, y vel"""
        # Update the x-coordinate
        self.x += self.x_vel
        # If dvdimage is too far to the left
        if self.x < 0:
            # Keep the object inside the canvas
            self.x = 0
            # Set the velocity to the negative
            self.x_vel = -self.x_vel
        # If dvdimage is too far to the right
        if self.x + self.width > SCREEN_WIDTH:
            # Keep the object inside the canvas
            self.x = SCREEN_WIDTH - self.width
            # Set the velocity to the negative
            self.x_vel = -self.x_vel

        # Update the y-coordinate
        self.y += self.y_vel
        # If dvdimage is too high to the top
        if self.y < 0:
            # Keep the object inside the canvas
            self.y = 0
            # Set the velocity to the negative
            self.y_vel = -self.y_vel
        # If dvdimage is too low to the bottom
        if self.y + self.height > SCREEN_HEIGHT:
            # Keep the object inside the canvas
            self.y = SCREEN_HEIGHT - self.height
            # Set the velocity to the negative
            self.y_vel = -self.y_vel


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
        dvd_image.update()
        print(f"x: {dvd_image.x}, y: {dvd_image.y}")

        # Draw the environment
        screen.fill(WHITE)      # fill with background color
        # for i in range(10):
        #     pygame.draw.rect(screen, RED, [100 + i * 10, 100 + i * 10, 75, 30])

        # pygame.draw.circle(screen, BLUE, [500, 150], 50)

        # .blit(<surface/image>, coords)
        screen.blit(dvd_image.img, (dvd_image.x, dvd_image.y))

        # Draw our Dvdimage
        # pygame.draw.rect(screen, dvd_image.colour, dvd_image.rect())  # method

        # Update the screen
        pygame.display.flip()

        # Tick the clock
        clock.tick(60)


if __name__ == "__main__":
    main()
