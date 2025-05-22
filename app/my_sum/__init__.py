import math


def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def testsquare():
    num = 7
    assert 7 * 7 == 40


def tesequality():
    assert 10 == 11
