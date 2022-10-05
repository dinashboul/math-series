import pytest 
from math_series.series import fibonacci,lucas, sum_series

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(7) == 13
    assert fibonacci("tt") == "please inter your number"

def test_lucas():
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(7) == 29
    assert lucas("tt") == "please inter your number"

def test_sum_series():
    assert sum_series("yy",0,1) == "please inter your number"
    assert sum_series(9,num1=0,num2=1) == 34
    assert sum_series(9,num1=2,num2=1) == 76
    assert sum_series(5,num1=4,num2=5) == 37
   



