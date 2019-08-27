import string
from random import *
str1=string.printable

while True:
    for i in range(10):
        print(str1[randint(1,80)],end="")
    print()
    input()
