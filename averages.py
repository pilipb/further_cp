#!/usr/bin/env python3

import sys

# take command line inputs and calculate the mean, median, and mode depending on flags

all_args = sys.argv[1:]

# identify flags
flags = []
if "--mean" in all_args:
    flags.append("mean")
if "--median" in all_args:
    flags.append("median")
if "--mode" in all_args:
    flags.append("mode")

# remove flags from list of arguments
for flag in flags:
    all_args.remove("--" + flag)

# convert arguments to floats
try:
    for i in range(len(all_args)):
        all_args[i] = float(all_args[i])
except ValueError:
    print("Invalid argument(s) inputted")
    exit()

# calculate mean, median, and mode

def mean(args):
    return sum(args) / len(args)

def median(args):
    args.sort()
    if len(args) % 2 == 0:
        return (args[len(args) // 2] + args[len(args) // 2 - 1]) / 2
    else:
        return args[len(args) // 2]

def mode(args):
    mode = args[0]
    mode_count = 0
    for arg in args:
        arg_count = 0
        for arg2 in args:
            if arg == arg2:
                arg_count += 1
        if arg_count > mode_count:
            mode = arg
            mode_count = arg_count
    return mode

mean = mean(all_args)
median = median(all_args)
mode = mode(all_args)

if len(all_args) == 0:
    print("No arguments inputted")
    exit()
elif len(flags) == 0:
    print("No flags inputted")
    print(mean)
    print(median)
    print(mode)
    exit()
else:
    for flag in flags:
        if flag == "mean":
            print(mean)
        elif flag == "median":
            print(median)
        elif flag == "mode":
            print(mode)
    exit()




