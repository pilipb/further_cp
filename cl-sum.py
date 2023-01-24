#!/usr/bin/env python3

import sys

# get first 5 command line arguments

args = sys.argv
if len(args) > 6:
    args = args[1:6]
    print("Only the first 5 arguments will be used.")
else:
    args = args[1:]
    print("All", len(args), "arguments will be used.")





# sum the first 5 command line arguments
sum = 0
for arg in args:
    try:
        sum += int(arg)
    except ValueError:
        print("Invalid argument:", arg)

# print the sum
print(sum)

