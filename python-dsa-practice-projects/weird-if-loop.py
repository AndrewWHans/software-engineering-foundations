# Given an integer, n, perform the following conditional actions:
# if n is odd, print Weird
# if n is even and in the inclusive range of 2 to 5, print Not Weird
# if n is even and in the inclusive range of 6 to 20, print Weird
# if n is even and greater than 20, print Not Weird

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
