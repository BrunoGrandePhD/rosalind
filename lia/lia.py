#!/usr/bin/env python

import math
import sys


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def lia(k, N):
    pop_num = 2 ** k
    total_prob = 0
    for num in range(N, pop_num+1):
        prob = (0.25 ** num) * (0.75 ** (pop_num - num)) * nCr(pop_num, num)
        total_prob += prob
    return total_prob


if __name__ == '__main__':
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[2], "w")
    k, N = [int(num) for num in infile.read().rstrip().split(" ")]
    outfile.write(str(lia(k, N)))
