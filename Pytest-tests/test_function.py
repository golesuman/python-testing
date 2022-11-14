import math
import pytest


def func_sqrt(x):
    return math.sqrt(x)


@pytest.mark.number
def test_sqrt():
    x = 25
    value = func_sqrt(x)
    assert value == 5




def check_str(x):
    return True if type(x) == str else None


@pytest.mark.strings
def test_str_type():
    a = check_str('5')
    assert a == True



@pytest.fixture
def input_value():
    input_ = 39
    return input_


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0


