import pytest


@pytest.yield_fixture()
def setUp():
    print("Run Once befor each test")
    yield
    print("Run once after each test")

def test_Demo2_methodA(setUp):
    print("Running test A")

def test_Demo2_methodB(setUp):
    print("Running test B")