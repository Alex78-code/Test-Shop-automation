"""# 1.Регистрация нового пользователя
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_link_text("My Account").click()
email_address = driver.find_element_by_id("reg_email")
email_address.click()
email_address.send_keys("bimove@mailinator.com")
password = driver.find_element_by_id("reg_password")
password.click()
time.sleep(2)
password.send_keys("phz077BPL")
register = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row>:nth-child(3)").click()
driver.quit()"""

"""# 2.Вход на сайт
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
# Переход на вкладку Мой аккаунт, заполнение полей
my_account = driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("bimove@mailinator.com")
password = driver.find_element_by_id("password")
password.send_keys("phz077BPL")
login = driver.find_element_by_css_selector(".login>:nth-child(3) .woocommerce-Button").click()
# Проверка присутствия элемента Logout
wait = WebDriverWait(driver,10)
logout = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".woocommerce-MyAccount-navigation>ul>:nth-child(6)>a")))
driver.quit()"""