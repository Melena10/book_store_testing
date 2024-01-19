'''4. Shop: отображение страницы товара'''
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
shop = driver.find_element_by_css_selector("#menu-item-40 a")
shop.click()
html_5_forms = driver.find_element_by_css_selector(".post-181 img")
html_5_forms.click()
h1 = driver.find_element_by_css_selector(".summary h1")
h1_get_text = h1.text
assert h1_get_text == "HTML5 Forms"
driver.quit()
'''

'''5. Shop: количество товаров в категории'''
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector("#menu-item-50 a")
my_account.click()
time.sleep(3)
login_email = driver.find_element_by_id("username")
login_email.send_keys("eakudinova1980@gmail.com")
login_password = driver.find_element_by_id("password")
login_password.send_keys("123!@#NNNkkk")
login_btn = driver.find_element_by_css_selector(".login .woocommerce-Button")
login_btn.click()
shop = driver.find_element_by_css_selector("#menu-item-40 a")
shop.click()
time.sleep(3)
html_tab = driver.find_element_by_css_selector(".cat-item-19 a")
html_tab.click()
time.sleep(3)
product1 = driver.find_element_by_css_selector(".masonry-done .post-181")
product2 = driver.find_element_by_css_selector(".masonry-done .post-182")
product3 = driver.find_element_by_css_selector(".masonry-done .post-163")
driver.quit()
'''

'''6. Shop: сортировка товаров'''
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector("#menu-item-50 a")
my_account.click()
time.sleep(3)
login_email = driver.find_element_by_id("username")
login_email.send_keys("eakudinova1980@gmail.com")
login_password = driver.find_element_by_id("password")
login_password.send_keys("123!@#NNNkkk")
login_btn = driver.find_element_by_css_selector(".login .woocommerce-Button")
login_btn.click()
shop = driver.find_element_by_css_selector("#menu-item-40 a")
shop.click()
time.sleep(3)
select_form = driver.find_element_by_class_name("orderby").click()
value = driver.find_element_by_css_selector("[value='menu_order']").click()
time.sleep(3)
from selenium.webdriver.support.select import Select
element = driver.find_element_by_class_name("orderby")
select = Select(element)
select.select_by_value("price-desc")
element = driver.find_element_by_class_name("orderby").click()
sort = driver.find_element_by_css_selector("[value='price-desc']")
'''

'''7. Shop: отображение, скидка товара'''

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector("#menu-item-50 a")
my_account.click()
time.sleep(3)
login_email = driver.find_element_by_id("username")
login_email.send_keys("eakudinova1980@gmail.com")
login_password = driver.find_element_by_id("password")
login_password.send_keys("123!@#NNNkkk")
login_btn = driver.find_element_by_css_selector(".login .woocommerce-Button")
login_btn.click()
shop = driver.find_element_by_css_selector("#menu-item-40 a")
shop.click()
time.sleep(3)
book_android = driver.find_element_by_css_selector(".post-169 .woocommerce-LoopProduct-link")
book_android.click()
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
cover_book = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, ".attachment-shop_single.size-shop_single.wp-post-image")))
cover_book.click()
cover_close = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
cover_close.click()
'''

'''8. Shop: проверка цены в корзине'''

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector("#menu-item-50 a")
my_account.click()
time.sleep(3)
login_email = driver.find_element_by_id("username")
login_email.send_keys("eakudinova1980@gmail.com")
login_password = driver.find_element_by_id("password")
login_password.send_keys("123!@#NNNkkk")
login_btn = driver.find_element_by_css_selector(".login .woocommerce-Button")
login_btn.click()
shop = driver.find_element_by_css_selector("#menu-item-40 a")
shop.click()
time.sleep(3)
book_development_basket = driver.find_element_by_css_selector(".post-182 .button")
book_development_basket.click()
basket_item = driver.find_element_by_css_selector(".wpmenucartli .cartcontents")
basket_item_text = basket_item.text
assert basket_item_text == "1 Item"
basket_amount = driver.find_element_by_css_selector(".wpmenucartli .amount")
basket_amount = basket_amount.text
assert basket_amount == "₹180.00"
basket = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
basket.click()
basket_subtotal = WebDriverWait(driver, 10).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
basket_total = WebDriverWait(driver, 10).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-subtotal .woocommerce-Price-amount"), "₹180.00"))
driver.quit()
'''

'''9. Shop: работа в корзине'''

'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop = driver.find_element_by_css_selector("#menu-item-40 a")
shop.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")
book_development_basket = driver.find_element_by_css_selector(".post-182 .button")
book_development_basket.click()
time.sleep(3)
book_JS_Data_Structures = driver.find_element_by_css_selector(".post-180 .button")
book_JS_Data_Structures.click()
time.sleep(3)
basket = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
basket.click()
time.sleep(3)
remove_btn_1 = driver.find_element_by_css_selector(".cart_item:nth-child(2) .remove")
remove_btn_1.click()
time.sleep(3)
undo_btn = driver.find_element_by_css_selector(".woocommerce-message > a")
undo_btn.click()
quantity = driver.find_element_by_css_selector(".cart_item:nth-child(2) .quantity input")
quantity.clear()
quantity.send_keys("3")
time.sleep(3)
update_basket_btn = driver.find_element_by_css_selector("[name='update_cart']")
update_basket_btn.click()
time.sleep(3)
quantity = driver.find_element_by_css_selector(".cart_item:nth-child(2) .quantity input")
quantity_get_text = quantity.text
assert quantity_get_text == "3"
apply_coupon_btn = driver.find_element_by_css_selector("[name='apply_coupon']")
time.sleep(3)
apply_coupon_btn.click()
message = driver.find_element_by_css_selector(".woocommerce-error li")
message_get_text = message.text
assert message_get_text == "Please enter a coupon code."
driver.quit()
'''

'''10. Shop: покупка товара'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop = driver.find_element_by_css_selector("#menu-item-40 a")
shop.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")
book_development_basket = driver.find_element_by_css_selector(".post-182 .button")
book_development_basket.click()
time.sleep(3)
basket = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
basket.click()
time.sleep(3)
proceed_btn = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
proceed_btn.click()
time.sleep(3)
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Elena")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Kudinova")
email = driver.find_element_by_id("billing_email")
email.send_keys("eakudinova1980@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("+7999999999")
time.sleep(3)
country_select = driver.find_element_by_id("s2id_billing_country").click()
country_input = driver.find_element_by_id("s2id_autogen1_search")
country_input.send_keys("Russia")
country_search = driver.find_element_by_css_selector("#select2-result-label-1782 span")
country_search.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Street")
town = driver.find_element_by_id("billing_city")
town.send_keys("Moscow")
state = driver.find_element_by_id("billing_state")
state.send_keys("State")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("123456")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
payments = driver.find_element_by_id("payment_method_cheque")
payments.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
message_text = WebDriverWait(driver, 10).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

payment_method = WebDriverWait(driver, 10).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table tr:nth-child(3) td"), "Check Payments"))
