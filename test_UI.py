import yaml
from testpage import OperationsHelper
import time
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

login = testdata['login']
password = testdata['password']
alert_text = testdata['alert_text']

def test_step_1(browser):
    logging.info("Test 1 starting (UI)")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(1)
    testpage.enter_login("Test")
    testpage.enter_pass("Test")
    testpage.click_login_btn()
    assert testpage.get_error_text() == "401"

def test_step_2(browser):
    logging.info("Test 2 starting (UI)")
    testpage = OperationsHelper(browser)
    testpage.enter_login(login)
    time.sleep(1)
    testpage.enter_pass(password)
    testpage.click_login_btn()
    assert testpage.get_auth_text() == f"Hello, {login}"

def test_step_3(browser):
    logging.info("Test 3 starting (UI)")
    testpage = OperationsHelper(browser)
    testpage._add_post_btn()
    time.sleep(1)
    title = "Test_3"
    testpage.fill_post_info(title=title, description="Test_3", content="Test_3")
    time.sleep(1)
    testpage.create_post_btn()
    time.sleep(1)
    assert testpage.get_title_text() == title

def test_step_4(browser):
    logging.info("Test 4 starting (UI)")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage._add_post_btn()
    time.sleep(1)
    title = "Test_4"
    testpage.fill_post_info(title=title, description="Test_4")
    time.sleep(1)
    testpage.create_post_btn()
    time.sleep(1)
    assert testpage.get_title_text() == title

def test_step_5(browser):
    logging.info("Test 5 starting (UI)")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage._add_post_btn()
    time.sleep(1)
    title = "Test_5"
    testpage.fill_post_info(title="Test_5", content="Test_5")
    time.sleep(1)
    testpage.create_post_btn()
    time.sleep(1)
    assert testpage.get_title_text() == title

def test_step_6(browser):
    logging.info("Test 6 starting (UI)")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage._add_post_btn()
    time.sleep(1)
    title = "Test_6"
    testpage.fill_post_info(title="Test_6")
    time.sleep(1)
    testpage.create_post_btn()
    time.sleep(1)
    assert testpage.get_title_text() == title

def test_step_7(browser):
    logging.info("Test 7 starting (UI)")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(1)
    testpage.contact_form_open_btn()
    time.sleep(1)
    testpage.fill_contact_form(name='Pedro Pascal', email='qwerty123@ya.ru', content='Some good words')
    testpage.contact_form_send_btn()
    time.sleep(1)
    assert testpage.get_alert() == alert_text