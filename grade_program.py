#!/usr/bin/env python3

# Created by: Tamer Zreg
# Date: Nov.28, 2022
# This program calculates the middle mark of a level


# Defining middle mark function
def MidMark(level):

    # Match case statement structure used for each possible level value
    match level:
        case "4+":
            return "97.5%"
        case "4":
            return "90.5%"
        case "4-":
            return "83%"
        case "3+":
            return "78%"
        case "3":
            return "74%"
        case "3-":
            return "71%"
        case "2+":
            return "68%"
        case "2":
            return "64.5%"
        case "2-":
            return "61%"
        case "1+":
            return "58%"
        case "1":
            return "54.5%"
        case "1-":
            return "51%"
        case "R":
            return "24.5%"
        case _:
            return "-1"


def main():
    # Getting the level from the user3. Makes input uppercase for
    # remediation case
    user_level = input("Enter a level: ").upper()

    # Storing return value inside the percentage variable
    percentage = MidMark(user_level)

    # Body code executed if the user entered an invalid level
    if percentage == "-1":
        print(f"{user_level} is not a valid level.")

    else:
        # Displays the middle mark to the user
        print(f"The middle mark of {user_level} is {percentage}")


if __name__ == "__main__":
    main()
