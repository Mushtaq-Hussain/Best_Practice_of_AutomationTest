import pytest


@pytest.fixture()
def setUp():
    print("Running setUp")

def test_Demo1_methodA(setUp):
    print("Running test A")

def test_Demo1_methodB(setUp):
    print("Running test B")
