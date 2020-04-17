import pytest


@pytest.mark.smoke
def test_newFile():
    a = 3
    b = 7
    assert a+4 == b, "Numbers do not match"


# @pytest.mark.skip
@pytest.mark.xfail
def test_practice(setup):
    msg = "New test module"
    assert msg == "New test module", "String mismatch"
