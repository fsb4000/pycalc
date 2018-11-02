#!/usr/bin/python3

import sys

def add(a, b):
    return float(a) + float(b)

if __name__ == '__main__':
    assert (len(sys.argv) == 3),"Wrong numbers arguments"
    print ( add(sys.argv[1], sys.argv[2]) )
