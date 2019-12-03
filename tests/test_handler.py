import pytest
from datetime import datetime, timedelta


# content of test_sample.py
# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(3) == 4
#
#
# testdata = [
#     (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
#     (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
# ]
#
#
# @pytest.mark.parametrize("a,b,expected", testdata)
# def test_timedistance_v0(a, b, expected):
#     diff = a - b
#     assert diff == expected
#
#
# @pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
# def test_timedistance_v1(a, b, expected):
#     diff = a - b
#     assert diff == expected
