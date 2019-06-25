import unittest
from selenium import webdriver
import time

class UnitTestCase(unittest.TestCase):
    def test_reg1(self):
        link = " http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element_by_class_name("first").send_keys("Andr")
        browser.find_element_by_class_name("second").send_keys("Mor")
        browser.find_element_by_class_name("third").send_keys("xxx")
        browser.find_element_by_tag_name("button").click()
        time.sleep(1)
        welcome_text_alt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_alt.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)
        
    def test_abs2(self):
        link = " http://suninjuly.github.io/registration2.html "
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element_by_css_selector(" div.first_block input.form-control.first ").send_keys("Andr")
        browser.find_element_by_css_selector(" div.first_block input.form-control.second ").send_keys("Mor")
        browser.find_element_by_css_selector(" div.first_block input.form-control.third ").send_keys("xxx")
        browser.find_element_by_tag_name(" button ").click()
        time.sleep(1)
        welcome_text_alt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_alt.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)
        
if __name__ == "__main__":
    unittest.main()
