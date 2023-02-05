#!/usr/bin/env python3

import sys
import numpy as np

# calculate mean, median, and mode

def mean(args):
    return np.mean(args)
def median(args):
    return np.median(args)
def mode(args):
    return np.mode(args)


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
if "--file" in all_args:
    flags.append("file")


# remove flags from list of arguments
for flag in flags:
    all_args.remove("--" + flag)

# open file if flag is present
if "file" in flags:
    
    try:
        file = open(all_args[-1], "r")
        all_args = file.read().split()
        print(all_args)

        # convert list all_args to floats
        for i in range(len(all_args)):
            all_args[i] = float(all_args[i])

        for flag in flags:
            if flag == "mean":
                mean = mean(all_args)
                print(mean)
            if flag == "median":
                median = median(all_args)
                print(median)
            if flag == "mode":
                mode = mode(all_args)
                print(mode)
            else:
                print("Invalid flag inputted")
                exit()
        
    except NameError:
        print("File not found")
        exit()


# convert arguments to floats
try:
    for i in range(len(all_args)):
        all_args[i] = float(all_args[i])
except ValueError:
    print("Invalid argument(s) inputted")
    exit()



if len(flags) == 0:
    print("No flags inputted")
    try:
        mean = mean(all_args)
        median = median(all_args)
        mode = mode(all_args)
    except ZeroDivisionError:
        print("No arguments inputted")
        exit()
    print(mean)
    print(median)
    print(mode)
    exit()
else:
    for flag in flags:
        try:
            if flag == "mean":
                mean = mean(all_args)
                print(mean)
            elif flag == "median":
                median = median(all_args)
                print(median)
            elif flag == "mode":
                mode = mode(all_args)
                print(mode)
        except ZeroDivisionError:
            print("No arguments inputted")
            exit()







