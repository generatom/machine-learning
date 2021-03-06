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

class TestComments():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_comments(self):
    self.driver.get("https://pentesttools.co.uk/")
    self.driver.set_window_size(1280, 775)
    self.driver.find_element(By.CSS_SELECTOR, ".footer-widgets-outer-wrapper").click()
    self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(2) > .page-item-55 > a").click()
    self.driver.find_element(By.ID, "comment").click()
    self.driver.find_element(By.ID, "comment").send_keys("Some text")
    self.driver.find_element(By.ID, "author").send_keys("Jono")
    self.driver.find_element(By.ID, "url").send_keys("noweb.com")
    self.driver.find_element(By.ID, "email").send_keys("jono.n@test.com")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.ID, "div-comment-6").click()
  
