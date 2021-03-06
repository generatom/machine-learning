#!/usr/bin/env python3
# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestStart():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_start(self):
    # Test name: start
    # Step # | name | target | value
    # 1 | open | / |
    self.driver.get("https://pentesttools.co.uk/")
    # 2 | setWindowSize | 1280x775 |
    self.driver.set_window_size(1280, 775)
    # 3 | click | css=ul:nth-child(2) > .page-item-55 > a |
    self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(2) > .page-item-55 > a").click()
    # 4 | click | id=nf-field-1 |
    self.driver.find_element(By.ID, "nf-field-1").click()
    # 5 | type | id=nf-field-1 | Jono
    self.driver.find_element(By.ID, "nf-field-1").send_keys("Jono")
    # 6 | type | id=nf-field-2 | Nicholas
    self.driver.find_element(By.ID, "nf-field-2").send_keys("Nicholas")
    # 7 | click | id=nf-field-2 |
    self.driver.find_element(By.ID, "nf-field-2").click()
    # 8 | type | id=nf-field-2 | jono.nicholas@test.com
    self.driver.find_element(By.ID, "nf-field-2").send_keys("jono.nicholas@test.com")
    # 9 | type | id=nf-field-3 | This is a test of selenium.
    self.driver.find_element(By.ID, "nf-field-3").send_keys("This is a test of selenium.")
    # 10 | click | id=nf-field-4 |
    self.driver.find_element(By.ID, "nf-field-4").click()
