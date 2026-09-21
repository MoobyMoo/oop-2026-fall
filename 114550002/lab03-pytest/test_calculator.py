import pytest
from calculator import add
from calculator import devide

def test_add_two_number():
    assert add(2, 3) == 5

def test_devide_two_number():
    with pytest.raises(ValueError):
        devide(5, 0)