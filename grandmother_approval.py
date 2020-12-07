#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program determines if grandmother will approve
#       the user dating her grandchild

import constants


def main():
    # this function will determine if the user is in the
    #       age range

    print("This program determines if you can date "
          "Grandmother's grandchild")

    # input
    user_age = input("Enter your age as an integer: ")
    print("")

    # process
    try:
        user_age_int = int(user_age)

        if user_age_int > constants.MIN_AGE and \
           user_age_int < constants.MAX_AGE:
            # output
            print("Congrats! Grandmother will approve of you"
                  " dating her grandchild.")
        else:
            # output
            print("Sorry, Grandmother wants someone over"
                  " {0} and under {1}..."
                  .format(constants.MIN_AGE, constants.MAX_AGE))
    except Exception:
        # output
        print("That's not a number! Try again.")
    finally:
        # output
        print("")
        print("Good luck with your dating life.")


if __name__ == "__main__":
    main()
