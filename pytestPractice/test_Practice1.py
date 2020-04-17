# All the testing file should start with the test_ keyword or end with _test
# Test method name should start with test
# All the test code to be wrapped in the method
# -k method name selection for execution
# -s los, -v more info about test
# -m mark(tag),to run only marked test cases Ex:-@pytest.mark.smoke
import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "Good Morning"
    assert msg == "Good Morning"


def test_addFun():
    res = 5 + 6
    assert res == 11


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])


