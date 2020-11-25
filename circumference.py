#!/usr/bin/env python3
# Created by: Roman Cernetchi
# Created on: November 2020
# This program calculates circumference

import constants


def main():
    # This function calculates circumference

    # Input
    radius = int(input("Enter the radius of a circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # Output
    print("")
    print("Circumference is {}mm^2".format(circumference))


if __name__ == "__main__":
    main()
