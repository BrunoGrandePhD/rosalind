#!/usr/bin/env python

import sys


def subs(s, t):
    idxs = []
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            idxs.append(i)
    return " ".join([str(idx + 1) for idx in idxs])


if __name__ == '__main__':
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[2], "w")
    s, t = [line.rstrip() for line in infile.readlines()]
    outfile.write(subs(s, t))
