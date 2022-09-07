from __future__ import absolute_import

from calculations import absolute


def test_absolute_with_positive():
    input = 5
    result = absolute(input)
    expected = 5
    assert result == expected


def test_absolute_with_negative():
    assert absolute(-5) == 5

def test_absolute_with_zero():
    assert absolute(0) == 0