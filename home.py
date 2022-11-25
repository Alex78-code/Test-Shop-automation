# 1.Добавление комментария
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
#Скролл страницы
driver.execute_script("window.scrollBy(0,700);")
# Выбор книги и написание комментария
selenium_ruby = driver.find_element_by_css_selector(".post-160 .woocommerce-LoopProduct-link").click()
reviews = driver.find_element_by_css_selector(".reviews_tab>a").click()
star_5 = driver.find_element_by_link_text("5").click()
review = driver.find_element_by_id("comment")
review.send_keys("Nice books!")
# Заполнение полей Имя и Почта, отправка
name = driver.find_element_by_id("author")
name.send_keys("Elvis")
email = driver.find_element_by_id("email")
email.send_keys("bimove@mailinator.com")
submit = driver.find_element_by_id("submit").click()
driver.quit()
