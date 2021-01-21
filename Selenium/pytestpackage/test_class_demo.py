import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestClass():
    @pytest.fixture(autouse=True)
    def classSetup(self,one_time_setup):
        self.abc = SomeClassToTest(self.value)

    def test_commandline_method1(self):
        result = self.abc.sum_numbers(5,10)
        assert result == 35
        print("Running test A")

    def test_commandline_method2(self):
        result = self.abc.sum_numbers(3,10)
        assert result == 33
        print("Running test b")