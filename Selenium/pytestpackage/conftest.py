import pytest


@pytest.yield_fixture()
def setup():
    print("Running Method level setUp")
    yield
    print("Running Method level tearDown")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("Running Conftest setUp one time before module")
    if browser == 'chrome':
        value = 10
        print("Running tests on Chrome")
    else:
        value = 20
        print("Running tests on FF")
    if request.cls is not None:
        request.cls.value = value
    yield value
    print("Running Conftest tearDown one time after module")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("osType")

