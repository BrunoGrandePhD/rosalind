#!/usr/bin/env python

from __future__ import division

import sys


def calc_prob(gt, k, m, n):
    """Calculate probably of picking individual
    of a certain genotype `gt` given the numbers
    k, m and n.

    gt values
    ---------
    0 -> homozygous recessive
    1 -> heterozygous
    2 -> homozygous dominant
    """
    total = k + m + n
    nums = [n, m, k]
    return nums[gt] / total


def iprb(k, m, n):
    # List of possible parent pairs (without replacement)
    prob_a = 1 * 1 * (calc_prob(2, k, m, n) * calc_prob(2, k-1, m, n))  # Two homozygous dominant
    prob_b = 2 * 1 * (calc_prob(2, k, m, n) * calc_prob(1, k-1, m, n))  # One homozygous dominant and one heterozygous
    prob_c = 1 * 0.75 * (calc_prob(1, k, m, n) * calc_prob(1, k, m-1, n))  # Two heterozygous
    prob_d = 2 * 0.5 * (calc_prob(1, k, m, n) * calc_prob(0, k, m-1, n))  # One heterozygous and one homozygous recessive
    prob_e = 2 * 1 * (calc_prob(2, k, m, n) * calc_prob(0, k-1, m, n))  # One homozygous dominant and one homozygous recessive
    return (prob_a + prob_b + prob_c + prob_d + prob_e)


if __name__ == '__main__':
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[2], "w")
    k, m, n = [int(num) for num in infile.read().rstrip().split(" ")]
    outfile.write(str(iprb(k, m, n)))
