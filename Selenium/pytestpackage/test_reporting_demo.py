import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestClass():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.abc = SomeClassToTest(10)

    def test_reporting_method1(self):
        result = self.abc.sum_numbers(5,10)
        assert result == 25
        print("Running test A")

    def test_reporting_method2(self):
        result = self.abc.sum_numbers(3,10)
        assert result == 23
        print("Running test b")