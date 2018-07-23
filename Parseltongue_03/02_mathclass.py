#!/usr/bin/env python3

# IDK
# By yhuang

from math import *
import sys
import statistics

def smallest( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min

def maximum( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

def average( list ):
    total = 0
    for x in list:
        total += x
    mean = total / len(list)
    return mean

def median(num):
    s_num = sorted(num)
    if len(num) % 2 == 1:
        return s_num[(len(num) / 2)]
    else:
        x = s_num[int((len(num) / 2) - 1)]
        y = s_num[(int(len(num) / 2))]
        z = x + y
    return int(z / 2)

def countX(list, x):
    count = 0
    for ele in list:
        if (ele == x):
            count = count + 1
    return count

def max_index(list, lenth):
    maxpos = list.index(max(list))
    return maxpos

def mode(list):
    list_n = []
    for x in list:
        a = countX(list, x)
        list_n.append(a)
    position = int(max_index(list_n,len(list)))
    return list[position] 


def range(list):
    x = maximum( list ) - smallest( list )
    return x

def main(args):
    arguments = sys.argv[1:]
    results = list(map(int, arguments))
    print("Min: ", end = '')
    print(smallest(results))
    print("Max: ", end = '')
    print(maximum(results))
    print("Mean: ", end = '')
    print(average(results))
    print("Median: ", end = '')
    print(median(results))
    print("mode: ", end = '')
    print(mode(results))
    print("Range: ", end = '')
    print(range(results))
    print("**************BONUS PART************")
    print(min(results))
    print(max(results))
    print(statistics.mean(results))
    print(statistics.median(results))
    print(statistics.mode(results))
    print(range(results))


if __name__ == "__main__":
    main(sys.argv)
