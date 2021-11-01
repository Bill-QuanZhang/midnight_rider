# Midnight Rider

import random
import time
import sys
import textwrap
import midnight_rider_text

# A text-based game of intrigue and illusion

# CONStANTS
MAX_FUEL = 50
MAX_TOFU = 3


class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is finished or not - bool
        distance_traveled: describe the distance that we've traveled so far this game, in km
        amount_of_tofu: how much tofu we have left in our inventory
        agents_distance: describes the distance between the player and the agents
        fuel: describes amount of fuel remaining, starts off 50
    """
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_of_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL

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
        # implement eating/hunger
        agents_distance_now = random.randrange(7, 15)

        if user_choice == "b":
            # implement slow traveling
            # Move the player
            player_distance_now = random.randrange(8, 14)
            self.distance_traveled += player_distance_now

            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now

            # Burn fuel
            self.fuel -= random.randrange(3, 9)

            # Give the player some feedback
            print(f"----------Wuu.")
            print(f"----------You traveled {player_distance_now} kms. \n")

        if user_choice == "c":
            # implement quick traveling
            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_traveled += player_distance_now

            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now

            # Burn fuel
            self.fuel -= random.randrange(5, 11)

            # Give the player some feedback
            print(f"----------ZOOM.")
            print(f"----------You traveled {player_distance_now} kms. \n")

        elif user_choice == "d":
            # Choice D - Refuel or Recharge
            self.fuel = MAX_FUEL

            # Decide how far the agents do
            self.agents_distance += agents_distance_now

            # Give the user feedback
            print(midnight_rider_text.REFUEL)
        elif user_choice == "e":
            print("-----Status Check-----")
            # print out distance traveled
            print(f"Distance Traveled: {self.distance_traveled} kms")
            print(f"Fuel Remaining: {self.fuel} L")
            # print out amount of tofu left
            print(f"Tofu Left: {self.amount_of_tofu} pieces")
            # print out AGENTS distance
            print(f"Agents Distance: {abs(self.agents_distance)} kms behind")
            print("----------")
            time.sleep(2)
        if user_choice == "q":
            self.done = True

def main() -> None:
    game = Game()   # starting a new game
    # game.introduction()

    # Main Loop:
    while not game.done:
        # Display the choices to the player
        game.show_choices()
        # Ask the player what they want to do
        # Change the state of the environment
        game.get_choice()
        # Check win/lose conditions


if __name__ == "__main__":
    main()
