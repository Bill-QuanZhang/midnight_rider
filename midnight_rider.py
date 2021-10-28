# Midnight Rider

import time
import sys
import textwrap
import midnight_rider_text

# A text-based game of intrigue and illusion


class Game:
    """Represent our game engine

    """
    def introduction(self) -> None:
        """Print the introduction text"""
        print(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect"""


def main() -> None:
    game = Game()   # starting a new game
    game.introduction()


if __name__ == "__main__":
    main()
