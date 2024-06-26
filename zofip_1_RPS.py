#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     12-03-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



A, B = input().split()


if A == B:
    print("D")

if A == "R" and B == "S":
    print("R")

if A == "S" and B=="R":
    print("R")


if A == "S" and B == "P":
    print("S")

if A == "P" and B=="S":
    print("S")

if A == "P" and B == "R":
    print("P")

if A == "R" and B=="P":
    print("P")