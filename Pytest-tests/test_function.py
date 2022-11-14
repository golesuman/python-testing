import math
import pytest


def func_sqrt(x):
    return math.sqrt(x)


@pytest.mark.filterwarnings
def test_sqrt():
    x = 25
    value = func_sqrt(x)
    assert value == 5




def check_str(x):
    return True if type(x) == str else None


@pytest.mark.filterwarnings
def test_str_type():
    a = check_str('5')
    assert a == True
