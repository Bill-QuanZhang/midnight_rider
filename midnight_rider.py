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
MAX_HUNGER = 50
MAX_DISTANCE = 100

ENDGAME_REASONS = {
    "LOSE_AGENTS": 1,
    "LOSE_FUEL": 2,
    "LOSE_HUNGER": 3,
    "WIN": 4
}


class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is finished or not - bool
        distance_traveled: describe the distance that we've traveled so far this game, in km
        amount_of_tofu: how much tofu we have left in our inventory
        agents_distance: describes the distance between the player and the agents
        fuel: describes amount of fuel remaining, starts off 50
        hunger: describe how hungry our player is, represented by a number 0-50,if hunger goes beyond 50, game is over
        endgame_reason: shows the index of teh game ending text from midnight_rider_text.py
    """
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_of_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = 0

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

        agents_distance_now = random.randrange(7, 15)

        # implement eating/hunger
        if user_choice == "a":
            # Consume one tofu IF and ONLY IF we have some available
            if self.amount_of_tofu > 0:
                self.amount_of_tofu -= 1

                # Decrease hunger to 0
                self.hunger = 0
                # Give the player some feedback
                # And text to midnight_rider_text.py
                print(midnight_rider_text.EAT_TOFU)
            else:
                # Tell the player they don't have tofu
                print(midnight_rider_text.NO_TOFU)

        elif user_choice == "b":
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

        elif user_choice == "c":
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

        elif user_choice == "q":
            self.done = True

        # Increase hunger
        if user_choice in ["b", "c", "d"]:
            self.hunger += random.randrange(8, 18)

    def upkeep(self) -> None:
        """Give the user reminders of hunger"""
        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)
        elif self.hunger > 25:
            print(midnight_rider_text.HUNGER)

        time.sleep(1)

    def check_endgame(self) -> None:
        """Check to see if win/lose conditions are met.
        If they're met, change the self.done flag."""
        # LOSE - Agents catch up to the player
        if self.agents_distance >= 0:
            # Allows us to quit the while loop
            self.done = True
            # Helps with printing the right ending
            self.endgame_reason = ENDGAME_REASONS["LOSE_AGENTS"]
        # LOSE - Fuel runs out
        if self.fuel <= 0:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_FUEL"]
        # LOSE - Perish because of hunger
        if self.hunger > MAX_HUNGER:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_HUNGER"]
        # WIN - Reach the goal
        if self.distance_traveled >= MAX_DISTANCE:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["WIN"]


def main() -> None:
    game = Game()   # starting a new game
    # game.introduction()

    # Main Loop:
    while not game.done:
        game.upkeep()
        # Display the choices to the player
        game.show_choices()
        # Ask the player what they want to do
        # Change the state of the environment
        game.get_choice()
        # Check win/lose conditions
        game.check_endgame()

    time.sleep(3)
    # PRINT OUT THE ENDING
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )


if __name__ == "__main__":
    main()
