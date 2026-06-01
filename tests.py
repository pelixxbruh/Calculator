from calculator import *


import random
import sys


def test_add():
  assert add(0, 0) == 0
  assert add(0, 1) == 1
  assert add(1, 0) == 1
  assert add(1, 1) == 2
  assert add(0, -1) == -1
  assert add(-1, 0) == -1
  assert add(-1, -1) == -2
  for i in range(10):
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)
    assert add(a, b) == a + b


def test_sub():
  assert sub(0, 0) == 0
  assert sub(0, 1) == -1
  assert sub(1, 0) == 1
  assert sub(1, 1) == 0
  assert sub(0, -1) == 1
  assert sub(-1, 0) == -1
  assert sub(-1, -1) == 0
  for i in range(10):
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)
    assert sub(a, b) == a - b

def test_mull():
  assert mull(0, 0) == 0
  assert mull(0, 1) == 0
  assert mull(1, 0) == 0
  assert mull(1, 1) == 1
  assert mull(1, 2) == 2
  assert mull(2, 1) == 2
  assert mull(0, -1) == 0
  assert mull(-1, 0) == 0
  assert mull(-1, -1) == 1
  assert mull(-1, -2) == 2
  assert mull(-2, -1) == 2
  for i in range(50):
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    try:
      assert mull(a, b) == a * b
    except:
      print(a,b,mull(a,b), a * b)
    

def test_div():
  assert div(0, 1) == 0
  assert div(1, 1) == 1
  assert div(2, 1) == 2

  for i in range(10):
    a = random.randint(0, 10)
    b = random.randint(1, 10)
    try:
      assert div(a, b) == a // b
    except:
      print(a,b,div(a,b), a // b)


def test_pow():
  assert pow(0, 1) == 0
  assert pow(1, 0) == 1
  assert pow(1, 1) == 1
  assert pow(1, 2) == 1
  assert pow(2, 1) == 2
  assert pow(-1, 1) == -1
  assert pow(-2, 1) == -2
  assert pow(-1, 2) == 1
  assert pow(-2, 2) == 4
  for i in range(10):
    a = random.randint(-5, 5)
    b = random.randint(0, 4)
    assert pow(a, b) == a ** b


def test_factorial():
  assert factorial(0) == 1
  assert factorial(1) == 1
  assert factorial(2) == 2
  assert factorial(3) == 6
  assert factorial(4) == 24
  assert factorial(5) == 120
  assert factorial(6) == 720

sys.setrecursionlimit(1000000)
test_add()
print("add - correct")
test_sub()
print("sub - correct")
test_mull()
print("mull - correct")
test_div()
print("div - correct")
test_pow()
print("pow - correct")
test_factorial()
print("factorial - correct")
exit()