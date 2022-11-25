# 1.Отображение страницы товара
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
# Логин в систему
my_account = driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("bimove@mailinator.com")
password = driver.find_element_by_id("password")
password.send_keys("phz077BPL")
login = driver.find_element_by_css_selector(".login>:nth-child(3) .woocommerce-Button").click()
# Нажатие вкладки Shop,выбор книги
shop = driver.find_element_by_link_text("Shop").click()
html_form = driver.find_element_by_css_selector(".post-181 .woocommerce-LoopProduct-link").click()
# Проверка заголовка
html_5_form = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div#pagewrap"),"HTML5 Forms")
)
driver.quit()

# 2 Количество товара в категории
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
# Логин в систему
my_account = driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("bimove@mailinator.com")
password = driver.find_element_by_id("password")
password.send_keys("phz077BPL")
# Преход на вкладку Shop
shop = driver.find_element_by_link_text("Shop").click()
# Выбор категории
category_html = driver.find_element_by_link_text("HTML").click()
# Проверка количества
items_html = len(driver.find_elements_by_class_name("woocommerce-LoopProduct-link"))
print(items_html)

# Или через if
"""if len(items_html)==3:
    print("На странице  3 товара")
else:
    print("Ошибка. Количество: "+ str(len(items_html)))"""
driver.quit()

# 3 Сортировка товаров
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
# Логин в систему
my_account = driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("bimove@mailinator.com")
password = driver.find_element_by_id("password")
password.send_keys("phz077BPL")
# Переход на вкладку Shop
shop = driver.find_element_by_link_text("Shop").click()
# Проверка варианта по умолчанию
order_by_default = driver.find_element_by_css_selector(".orderby>:nth-child(1)")
order_by_default_selected = order_by_default.get_attribute("selected")
if order_by_default_selected is not None:
    print("Селектор по умолчанию выбран")
else:
    print("Селектор по умолчанию не выбран")
# Сортировка от большей к меньшей
order_high_low = driver.find_element_by_css_selector("select.orderby").click()
high_low = driver.find_element_by_css_selector("option:nth-child(6)").click()
# Проверка смены значения в селекторе
order_by_default = driver.find_element_by_css_selector(".orderby>:nth-child(6)")
order_by_default_selected = order_by_default.get_attribute("selected")
if order_by_default_selected is not None:
    print("Селектор выбран от большего к меньшему")
else:
    print("Селектор неверно")
driver.quit()

# 4 Отображени,скидка товара
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
# Логин в систему
my_account = driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("bimove@mailinator.com")
password = driver.find_element_by_id("password")
password.send_keys("phz077BPL")
# Переход на вкладку Shop
shop = driver.find_element_by_link_text("Shop").click()
# Открытие карточки с товаром
android = driver.find_element_by_css_selector(".post-169 a.woocommerce-LoopProduct-link").click()
# Проверка старой цены
old_price = driver.find_element_by_css_selector(".price del .woocommerce-Price-amount.amount")
element_price = old_price.text
assert element_price == "₹600.00"
# Проверка новой цены
new_price = driver.find_element_by_css_selector(".price ins .woocommerce-Price-amount.amount")
element_price = new_price.text
assert element_price == "₹450.00"
# Ожидание и открытие предпросмотра картинки
wait = WebDriverWait(driver,5)
img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".attachment-shop_single.size-shop_single.wp-post-image")))
img_click = driver.find_element_by_css_selector(".attachment-shop_single.size-shop_single.wp-post-image").click()
# Ожидание и закрытие предпросмотра
close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.pp_close")))
close_btn = driver.find_element_by_css_selector("a.pp_close").click()
driver.quit()

# 5 Поверка цены в корзине
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
# Преход на вкладку Shop
shop = driver.find_element_by_link_text("Shop").click()
# Выбор и добавление книги в корзину
html_web_app = driver.find_element_by_css_selector(".products.masonry-done>:nth-child(4) .button").click()
time.sleep(1)
# Проверка отображения количества и стоймости
item = driver.find_element(By.CLASS_NAME,"cartcontents")
item_text = item.text
assert item_text == "1 Item"
price = driver.find_element(By.CSS_SELECTOR,".wpmenucart-contents .amount")
price_text = price.text
assert price_text == "₹180.00"
# Преход в корзину
basket = driver.find_element(By.CLASS_NAME,"wpmenucart-contents").click()
# Проверка отображения стоймости
wait = WebDriverWait(driver,5)
subtotal = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"cart-subtotal"),"₹180.00"))
total = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"order-total"),"₹183.60"))
driver.quit()

# 6 Работа в корзине
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
# Преход на вкладку Shop
shop = driver.find_element_by_link_text("Shop").click()
# Добавление книг и скролл страницы
html_web_app = driver.find_element(By.CSS_SELECTOR,".post-182 .button").click()
driver.execute_script("window.scrollBy(0,300);")
time.sleep(1)
js_data = driver.find_element(By.CSS_SELECTOR,".post-180 .button").click()
time.sleep(1)
# Преход в корзину
basket = driver.find_element(By.CLASS_NAME,"wpmenucart-contents").click()
time.sleep(1)
# Удаление первой книги
remove = driver.find_element(By.CSS_SELECTOR,'[data-product_id="182"]').click()
# Отмена удаления
undo = driver.find_element(By.LINK_TEXT,"Undo?").click()
# Увеличение количества товара
js_item = driver.find_element(By.CSS_SELECTOR,'[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
js_item.clear()
js_item.send_keys(3)
# Обновление корзины
update_basket = driver.find_element(By.CSS_SELECTOR,".actions>:nth-child(2)").click()
# Проверка значения, что товара 3
js_item = driver.find_element(By.CSS_SELECTOR,'[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
js_value = js_item.get_attribute("value")
assert js_value == "3"
time.sleep(1)
# Проверка появления сообщения
apple_coupon = driver.find_element(By.CSS_SELECTOR,'[name = "apply_coupon"]').click()
coupon = driver.find_element(By.CSS_SELECTOR,".page-content.entry-content .woocommerce-error")
coupon_text = coupon.text
assert coupon_text == "Please enter a coupon code."
print(coupon_text)
driver.quit()

# 7 Покупка товара
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
# Преход на вкладку Shop
shop = driver.find_element_by_link_text("Shop").click()
#Скролл страницы
driver.execute_script("window.scrollBy(0,300);")
#Добавление книги и переход в корзину
html_web_app = driver.find_element(By.CSS_SELECTOR,".post-182 .button").click()
time.sleep(1)
basket = driver.find_element(By.CLASS_NAME,"wpmenucart-contents").click()
# Ожидание и нажатие PROCEED TO CHECKOUT
wait = WebDriverWait(driver,5)
proceed = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".wc-proceed-to-checkout .checkout-button")))
proceed.click()
# Заполнение обязательных полей
first_name = wait.until(EC.presence_of_element_located((By.ID,"billing_first_name")))
firstName = driver.find_element(By.ID,"billing_first_name").send_keys("Ivan")
lastName = driver.find_element(By.ID,"billing_last_name").send_keys("Ivanov")
email = driver.find_element(By.ID,"billing_email").send_keys("nugexabij@mailinator.com")
phone = driver.find_element(By.ID,"billing_phone").send_keys("89991111111")
country = driver.find_element(By.ID,"select2-chosen-1").click()
country_search = driver.find_element(By.ID,"s2id_autogen1_search").send_keys("Austria")
country_enter = driver.find_element(By.CLASS_NAME,"select2-match").click()
address = driver.find_element(By.CSS_SELECTOR,"input#billing_address_1").send_keys("57 North Green Clarendon")
town = driver.find_element(By.CSS_SELECTOR,"input#billing_city").send_keys("Vienna")
postcode = driver.find_element(By.CSS_SELECTOR,"input#billing_postcode").send_keys("1020")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
# Выбор способа оплаты
payments = wait.until(EC.presence_of_element_located((By.ID,"payment_method_cheque"))).click()
place_older = driver.find_element(By.ID,"place_order").click()
#Проверка отображения текста
thank_you = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
check_payments = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".method strong"),"Check Payments"))
driver.quit()