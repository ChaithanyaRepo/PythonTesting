import pytest

from pytestPractice.baseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestExample:

    # When you pass the fixture fun name argument for the test fun then fixture fun is executed first
    def test_fixture(self):
        print("I will execute fixture test method")

    def test_fixture1(self):
        print("I will execute fixture test method1")

    def test_fixture2(self):
        print("I will execute fixture test method2")

    def test_fixture3(self):
        print("I will execute fixture test method3")

    def test_fixture4(self):
        print("I will execute fixture test method4")


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        # print(dataLoad[0])
        log.info(dataLoad[0])
        # print(dataLoad[1])
        log.info(dataLoad[1])
        # print(dataLoad[2])
        log.info(dataLoad[2])
