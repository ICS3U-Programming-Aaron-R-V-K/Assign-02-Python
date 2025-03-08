#!/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: March 6, 2025
# The code calculates the volume and area of a dodecahedron

import math
import colorama

colorama.init()


def main():
    while True:
        # Initial greeting to the user
        print(
            colorama.Fore.CYAN
            + "\nGreetings! In today's code, we are going to calculate the volume and surface area of a Dodecahedron.\n"
            + colorama.Fore.RESET
        )

        # Get the input of the edge length from the user
        edge_length = float(input("Enter the edge length of the dodecahedron (cm): "))

        # Formulas and calculations for volume and surface area
        volume = ((15 + 7 * math.sqrt(5)) / 4) * (edge_length**3)
        surface_area = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * (edge_length**2)

        # Display the results with 2 decimal places and colored text
        print(
            colorama.Fore.MAGENTA
            + "\nThe volume of the dodecahedron is: {:.2f} cm³".format(volume)
        )
        print(
            "The surface area of the dodecahedron is: {:.2f} cm²".format(surface_area)
            + colorama.Fore.RESET
        )
        # Ask the user if they want to do another calculation
        repeat = input("\nDo you want to calculate again? (yes/no): \n")

        if repeat != "yes":
            print(
                colorama.Fore.RED
                + "Goodbye! Thanks for using the Dodecahedron Calculator."
                + colorama.Fore.RESET
            )
            return  # return ends the loop and the program


if __name__ == "__main__":
    main()
