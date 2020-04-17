import pytest


@pytest.fixture(scope="class")
def setup():
    # This statement executed before test execution
    print("First execution")
    yield
    # This statement executed after test execution
    print("Last execution")
    # yield usage -> to close browser,clear memory, delete keys


@pytest.fixture()
def dataLoad():
    print("User profile data is collected")
    return ["Chaithanya", "B", "rahulshettyacademy.com"]


@pytest.fixture(params=[("Chrome", "Chaithanya"), ("Firefox", "Sushma"), ("IE", "Anusha")])
def crossBrowser(request):
    return request.param
