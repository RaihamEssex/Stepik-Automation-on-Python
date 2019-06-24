from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
driver = webdriver.Chrome(chrome_options=opt)
browser = webdriver.Chrome()

browser.get(" http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )
button1 = browser.find_element_by_id("book")
button1.click()

x_element = browser.find_element_by_id("input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
x = x_element.text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)


button2 = browser.find_element_by_id("solve").click()

