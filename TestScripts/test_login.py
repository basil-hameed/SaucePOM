"""
test_login file contains all the test cases
"""
from PageObjects.LoginPage import SauceLoginPage

def test_start():
    assert SauceLoginPage().start() == True
    print("SUCCESS : Automation Started !")

def test_login():
    assert SauceLoginPage().login() == True
    print("SUCCESS : Logged in !")

def test_shutdown():
    assert SauceLoginPage().shutdown() == None
    print("SUCCESS: Automation shutdown !")
