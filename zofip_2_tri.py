
import sys
exlist = list(map(int, sys.stdin.readline( ).split( ) ))
exlist.sort()
a = exlist[0]
b = exlist[1]
c = exlist[2]

if a + b <= c:
    print("0")
elif a**2 + b**2 == c**2:
    print("1")
elif a**2 + b**2 < c**2:
    print("2")
elif a**2 + b**2 > c**2:
    print("3")
