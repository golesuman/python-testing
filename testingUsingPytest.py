import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5



def testsquare():
    num = 5
    assert num**2 == 25


def testequality():
    num = 10
    assert num == 10


def test_greater():
    num = 10
    assert num > 5

def test_lesser():
    num = 20

    assert num < 200


def test_multiple():
    num = 2
    assert num%2 == 0


