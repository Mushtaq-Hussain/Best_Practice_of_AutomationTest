# Running test in multiple ways
# 1. py.test -v -s ==> Running all tests in PyTestPakages
# 2. py.test -v -s test_Demo.py  ==> Just run test_Demo2.py
# 3. py test -v -s test_Demo3.py::test_Demo3_methodA ==> just run method A in test_Demo3

import pytest


@pytest.yield_fixture()
def setUp():
    print("Running Demo 3 setUp")
    yield
    print("Running Demo 3 tearDown")

def test_Demo3_methodA(setUp):
    print("Running test A")

def test_Demo3_methodB(setUp):
    print("Running test B")