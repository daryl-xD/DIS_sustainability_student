from random import randint, seed
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


class Dice:
    def __init__(self, num_sides:int, num_dice:int):
        """
        Initialize a Dice object with the given number of sides and dice.

        Parameters:
        num_sides (int): Number of sides on each die.
        num_dice (int): Number of dice to roll.
        """
        self.num_sides = num_sides
        self.num_dice = num_dice

    @staticmethod
    def roll_dice(num_sides: int, num_dice: int) -> int:
        """
        Roll a specified number of dice with a given number of sides and sum the results.

        Parameters:
        num_sides (int): Number of sides on each die.
        num_dice (int): Number of dice to roll.

        Returns:
        int: Sum of the dice rolls.
        """
        # Sum the outcome of all dice rolls
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def simulate_rolls(self, num_rolls_sim: int) -> pd.DataFrame:
        """
        Simulate rolling the dice a specified number of times and store the results in a DataFrame.

        Parameters:
        num_rolls_sim (int): Number of times to roll the dice.

        Returns:
        pd.DataFrame: DataFrame containing the results of the dice rolls.
        """
        # Generate a list of roll results
        sim_rolls = [Dice.roll_dice(self.num_sides, self.num_dice) for _ in range(num_rolls_sim)]
        # Create a DataFrame from the list of roll results
        df_sim = pd.DataFrame({"rolls": sim_rolls})
        return df_sim

          
