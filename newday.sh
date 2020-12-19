#!/bin/bash

set -e

if [ $# -eq 0 ]; then
    echo "ERROR: DAY_NUM not supplied

usage: ./newday.sh DAY_NUM

DAY_NUM    day number" >&2
    exit 1
fi

if ! [[ $1 =~ '^[0-9]+$' ]]; then
    echo "ERROR: DAY_NUM must be an integer. Got $1.

usage: ./newday.sh DAY_NUM

DAY_NUM    day number" >&2
    exit 1
fi

DIR=day$1
TEST_INPUT=$DIR/test_input.txt
INPUT=$DIR/input.txt
SOLN=$DIR/soln.py

mkdir $DIR
echo "Created directory ./$DIR"
touch $TEST_INPUT
echo "Created file      ./$TEST_INPUT"
touch $INPUT
echo "Created file      ./$INPUT"

cat << HERE > $SOLN
def solve1(ipt, **kwargs):
    print('TODO: solve1')


def solve2(ipt, **kwargs):
    print('TODO: solve2')
HERE
echo "Created file      ./$SOLN"