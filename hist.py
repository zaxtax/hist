#!/usr/bin/env python3

import click
import numpy as np
import sys


def hist_strip(h):
    "Remove leading and trailing 0s in histogram"
    l = len(h[0])
    i = 0
    while h[0][i] == 0 and i < l:
        i += 1

    j = l
    while h[0][j-1] == 0 and j >= i:
        j -= 1

    return (h[0][i:j], h[1][i:j])


class IntOrStr(click.ParamType):
    name = 'int/str'

    def convert(self, value, param, ctx):
        try:
            return int(value)
        except ValueError:
            return value


@click.command()
@click.option('-d', '--discrete', is_flag=True)
@click.option('--bins',
              default="fd",
              type=IntOrStr(),
              help="""
                   Number of bins to use, or
                   a binning strategy (fd, sturges, sqrt, etc.)
                   """)
@click.option('--width', default=50, help='Max width for histogram.')
def hist(discrete, bins, width):
    data = np.fromiter(sys.stdin.readlines(), np.float)

    if discrete:
        h = tuple(reversed(np.unique(data, return_counts=True)))
    else:
        h = np.histogram(data, bins=bins)
    scale = max(h[0]) / width
    h = ((h[0] // scale).astype(int), h[1])
    h = hist_strip(h)

    for i in range(len(h[0])):
        if discrete:
            print("{: d}".format(int(h[1][i])), "="*h[0][i])
        else:
            print("{0: 0.2f}".format(h[1][i]), "="*h[0][i])


if __name__ == '__main__':
    hist()
