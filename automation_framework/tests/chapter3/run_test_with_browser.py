from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import pytest

# Chapter 3 - slide 6
def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.quit()

# Chapter 3 - slide 8
def test_open_firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.quit()

# Chapter 3 - slide 10
def test_open_edge():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.quit()