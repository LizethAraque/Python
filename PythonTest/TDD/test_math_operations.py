# test_math_operations.py

import pytest
from TDD.math_operations import *

def test_add():
    #ayuda a verificar que el comportamiento del codigo sea el esperado, en este caso el de ADD 
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(-2, -2) == -4

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
        
@pytest.mark.parametrize(
    "imput_x, imput_y, expected",
    [
        (3,5,9),
        (-1,add(0,1),0)
     ]
)
def test_sumados(imput_x, imput_y, expected):
    assert add(imput_x, imput_y) == expected