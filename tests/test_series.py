import pytest 
from math_series.series import fibonacci,lucas, sum_series

def test_fibonacci_zero():
    assert fibonacci(0) == 0
def test_fibonacci_one():    
    assert fibonacci(1) == 1
def test_fibonacci_two():
    assert fibonacci(2) == 1
def test_fibonacci_seven():
    assert fibonacci(7) == 13
def test_fibonacci_string():
    assert fibonacci("tt") == "please Enter your number"

def test_lucas_zero():
    assert lucas(0) == 2
def test_lucas_one():
    assert lucas(1) == 1
def test_lucas_two():
    assert lucas(2) == 3
def test_lucas_seven():
    assert lucas(7) == 29
def test_lucas_string():
    assert lucas("tt") == "please Enter your number"

def test_sum_series_string():
    assert sum_series("yy",0,1) == "please Enter your number"
def test_sum_series_fibo():
    assert sum_series(9,num1=0,num2=1) == 34
def test_sum_series_lucas():
    assert sum_series(9,num1=2,num2=1) == 76
def test_sum_series_other():
    assert sum_series(5,num1=4,num2=5) == 37
   



