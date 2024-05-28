from lohotron import check
import pytest


def test_check_lohotron():
    assert check(2) == "loh"
    assert check(3) == "neloh"