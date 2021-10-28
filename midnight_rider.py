# Midnight Rider

import time
import sys
import textwrap
import midnight_rider_text

# A text-based game of intrigue and illusion


class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is finished or not - bool
    """
    def __init__(self):
        self.done = False

    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect"""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes the environment"""
        # get the user's response
        user_choice = input().strip(",.?!").lower()

        # Based on their choice, change the attributes of class
        if user_choice == "q":
            self.done = True

def main() -> None:
    game = Game()   # starting a new game
    game.introduction()

    # Main Loop:
    while not game.done:
        # Display the choices to the player
        game.show_choices()
        # Ask the player what they want to do
        # Change the state of the environment
        # Check win/lose conditions


if __name__ == "__main__":
    main()
