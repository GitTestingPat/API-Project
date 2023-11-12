import pytest
from selenium import webdriver
from main import ShadyMeadowsPage
import time


def test_make_reservation():
    driver = webdriver.Chrome()
    page = ShadyMeadowsPage(driver)

    page.open()
    page.make_reservation("John", "Smith", "johnsmith@hotmail.com", "+123456789")
    time.sleep(5)

    driver.quit()
