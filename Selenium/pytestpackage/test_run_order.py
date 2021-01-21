import pytest


@pytest.mark.run(order=2)
def test_run_order_method1(one_time_setup, setup):
    print("Running test A")


@pytest.mark.run(order=1)
def test_run_order_method2(one_time_setup, setup):
    print("Running test B")


@pytest.mark.run(order=4)
def test_run_order_method3(one_time_setup, setup):
    print("Running test C")


@pytest.mark.run(order=6)
def test_run_order_method4(one_time_setup, setup):
    print("Running test D")


@pytest.mark.run(order=3)
def test_run_order_method5(one_time_setup, setup):
    print("Running test E")


@pytest.mark.run(order=5)
def test_run_order_method6(one_time_setup, setup):
    print("Running test F")