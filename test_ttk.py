from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time

link = "https://lk.ttk.ru/po/login.jsf"

@pytest.fixture
def browser():
    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nQuit browser..")
    browser.quit()

class TestLoginPage(object):
	def test_form_login(self, browser):
		browser.get(link)
		browser.find_element(By.ID, "ls").send_keys("615740741")
		time.sleep(1)
		check = browser.find_element(By.CSS_SELECTOR, "table tbody > tr td:nth-child(3) #loadingok").value_of_css_property('display')
		assert check == "block", "Login is too short or too small"
		browser.find_element(By.CSS_SELECTOR, "table tbody tr:nth-child(3) .form-text").send_keys("063072")
		browser.find_element(By.ID, "submit").click()
		time.sleep(2)
		schet = browser.find_element(By.ID, "accountNumber")
		schet_1 = schet.text
		assert "Лицевой счет №" in schet_1, "Page dont download"
