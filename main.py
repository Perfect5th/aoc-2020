#!/bin/env python

import importlib
import os
import sys


def read_input(ipt_fp):
    return [l.rstrip('\n') for l in ipt_fp]


if __name__ != '__main__':
    exit()

day_no = sys.argv[1]
test_only = len(sys.argv) > 2 and sys.argv[2] == '--test-only'
day_pkg = f'day{day_no}'
day = importlib.import_module(f'{day_pkg}.soln', package='day.subpkg')

with open(f'{day_pkg}/test_input.txt') as test_fp:
    test_ipt = read_input(test_fp)

if len(test_ipt) == 0:
    print('NO INPUT FOR TESTS')
    exit()

print('TEST')
day.solve1(test_ipt)

test_ipt_2 = f'{day_pkg}/test_input2.txt'
if os.path.exists(test_ipt_2):
    with open(test_ipt_2) as test_fp:
        test_ipt = read_input(test_fp)

day.solve2(test_ipt)
print('')

if test_only:
    exit()

with open(f'{day_pkg}/input.txt') as fp:
    ipt = read_input(fp)

if len(ipt) == 0:
    print('NO INPUT FOR PROBLEM')
    exit()

print('RESULT')
day.solve1(ipt)
day.solve2(ipt)
print('')