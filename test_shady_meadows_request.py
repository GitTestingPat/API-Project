import pytest
from selenium import webdriver
from main import ShadyMeadowsPage
import time


def test_make_request():
    driver = webdriver.Chrome()
    page = ShadyMeadowsPage(driver)

    page.open()
    message = "Quiero una habitación con vista al mar, cómoda, con baño en la habitación y cama extragrande. ¿Hay servicio a la habitación?"
    page.make_request("John Smith", "johnsmith@hotmail.com", "+123456789", "Hello", message)
    time.sleep(5)

    driver.quit()
