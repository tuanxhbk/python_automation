from selenium import webdriver
import pytest

# Chapter 3 - slide 11
def test_load_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.quit()

# Chapter 3 - slide 13
def test_current_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f"Current URL: {driver.current_url}")
    driver.quit()

# Chapter 3 - slide 15
def test_title():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f"The website's title: {driver.title}")
    driver.quit()

# Chapter 3 - slide 21
def test_back():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f"The website's title: {driver.title}")
    driver.get("https://www.google.com/")
    print(f"The website's title: {driver.title}")
    driver.back()
    print(f"The website's title: {driver.title}")
    driver.quit()

# Chapter 3 - slide 23
def test_forward():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f"The website's title: {driver.title}")
    driver.get("https://www.google.com/")
    print(f"The website's title: {driver.title}")
    driver.back()
    print(f"The website's title: {driver.title}")
    driver.forward()
    print(f"The website's title: {driver.title}")
    driver.quit()

# Chapter 3 - slide 25
def test_refresh():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f"Current URL: {driver.current_url}")
    driver.refresh()
    print(f"Current URL after refresh: {driver.current_url}")
    driver.quit()

# Chapter 3 - slide 27
def test_close():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.close()

# Chapter 3 - slide 28
def test_quit():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.quit()