from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
ruby = driver.find_element_by_css_selector(".post-160 h3")
ruby.click()
time.sleep(3)
reviews_btn = driver.find_element_by_css_selector(".reviews_tab a")
reviews_btn.click()
time.sleep(3)
star_1 = driver.find_element_by_class_name("star-1")
star_1.click()
star_2 = driver.find_element_by_class_name("star-2")
star_2.click()
star_3 = driver.find_element_by_class_name("star-3")
star_3.click()
star_4 = driver.find_element_by_class_name("star-4")
star_4.click()
star_5 = driver.find_element_by_class_name("star-5")
star_5.click()
time.sleep(3)
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")
time.sleep(3)
name = driver.find_element_by_id("author")
name.send_keys("Elena")
time.sleep(3)
email = driver.find_element_by_id("email")
email.send_keys("eakudinova1980@gmail.com")
time.sleep(3)
submit = driver.find_element_by_id("submit")
submit.click()
driver.quit()