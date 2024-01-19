'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector("#menu-item-50 a")
my_account.click()
register_email = driver.find_element_by_id("reg_email")
register_email.send_keys("eakudinova1980@gmail.com")
register_password = driver.find_element_by_id("reg_password")
register_password.send_keys("123!@#NNNkkk")
register_btn = driver.find_element_by_css_selector(".register .woocommerce-Button")
register_btn.click()
driver.quit()
'''

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector("#menu-item-50 a")
my_account.click()
login_email = driver.find_element_by_id("username")
login_email.send_keys("eakudinova1980@gmail.com")
login_password = driver.find_element_by_id("password")
login_password.send_keys("123!@#NNNkkk")
login_btn = driver.find_element_by_css_selector(".login .woocommerce-Button")
login_btn.click()
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout a")
driver.quit()
