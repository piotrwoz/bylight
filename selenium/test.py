import unittest
import os
import random
import string
import time
import names # pip install names
from selenium import webdriver # pip install selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.common.exceptions import NoSuchElementException

class TestUi(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\chromedrivers\\win\\chromedriver.exe")


    def add_to_cart(self,url, amount):
        driver = self.driver
        driver.get(url)
        i=0
        productsLeft = amount
        while productsLeft!=0:
            driver.get(url)

            product = driver.find_elements(By.CSS_SELECTOR,".product-title > a")[random.randint(0,11)]
            driver.get(product.get_attribute("href"))
            try:
                quantity = driver.find_elements(By.CSS_SELECTOR,".product-quantities > span")[0].get_attribute("data-stock")
                numOfProducts = random.randint(1,int(quantity))-1
                addBtn = driver.find_elements(By.CSS_SELECTOR,".btn.btn-touchspin.js-touchspin.bootstrap-touchspin-up")[0]
                for _ in range(0,random.randint(0,min(numOfProducts,10))):
                    addBtn.click()

                driver.find_elements(By.CSS_SELECTOR,".add-to-cart")[0].click()
                productsLeft-=1
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "blockcart-modal")))
            except Exception:
                i+=1
                


    def remove_from_cart(self):
        driver = self.driver
        driver.get("https://localhost/koszyk?action=show")
        delBtn = driver.find_elements(By.CSS_SELECTOR,"i.material-icons.float-xs-left")[0]
        delBtn.click()


    def fill_personal_data(self):
        driver = self.driver
        driver.get("https://localhost/zam%C3%B3wienie")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".radio-inline")))
        driver.find_elements(By.CSS_SELECTOR,".radio-inline")[0].click()

        firstNameField = driver.find_element(By.XPATH,'//input[@name="firstname"]')
        firstNameField.clear()
        firstName = names.get_first_name()
        firstNameField.send_keys(firstName)

        lastNameField = driver.find_element(By.XPATH,'//input[@name="lastname"]')
        lastNameField.clear()
        lastName = names.get_last_name()
        lastNameField.send_keys(lastName)

        emailField = driver.find_element(By.XPATH,'//input[@name="email"]')
        emailField.clear()
        email = firstName + "." + lastName + "@gmail.com"
        emailField.send_keys(email)

        letters = string.ascii_letters
        pswrdField = driver.find_element(By.XPATH,'//input[@name="password"]')
        pswrdField.clear()
        password = (''.join(random.choice(letters) for i in range(random.randint(8,15))))
        pswrdField.send_keys(password)

        driver.find_element(By.XPATH,'//input[@name="customer_privacy"]').click()
        submitBtn = driver.find_element(By.XPATH,'//button[@name="continue"]')

        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", submitBtn)
        driver.find_element(By.XPATH,'//input[@name="psgdpr"]').click()
        submitBtn.click()


    def fill_address(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="address1"]')))

        letters = string.ascii_letters

        address = driver.find_element(By.XPATH,'//input[@name="address1"]')
        address.clear()
        address.send_keys((''.join(random.choice(letters) for i in range(random.randint(8,15)))))

        postalFiled = driver.find_element(By.XPATH,'//input[@name="postcode"]')
        postalFiled.clear()
        postalFiled.send_keys("00-000")

        cityField = driver.find_element(By.XPATH,'//input[@name="city"]')
        cityField.clear()
        cityField.send_keys(names.get_last_name())

        submitBtn = driver.find_element(By.XPATH,'//button[@name="confirm-addresses"]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", submitBtn)
        submitBtn.click()


    def pick_delivery(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()[contains(., "DPD")]]')))

        match (random.randint(0,1)):
            case 0:
                driver.find_element(By.XPATH,'//*[text()[contains(., "DPD")]]').click()
            case 1:
                driver.find_element(By.XPATH,'//*[text()[contains(., "DHL")]]').click()
            
        
        submitBtn = driver.find_element(By.XPATH,'//button[@name="confirmDeliveryOption"]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", submitBtn)
        submitBtn.click()


    def choose_payment(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()[contains(., "Zapłać gotówką przy odbiorze")]]'))) # trzeba zmienić na  zapłać gotówką

        driver.find_element(By.XPATH,'//*[text()[contains(., "Zapłać gotówką przy odbiorze")]]').click()
        driver.find_element(By.XPATH,'//input[@name="conditions_to_approve[terms-and-conditions]"]').click()

        submitBtn = driver.find_element(By.XPATH,'//*[text()[contains(., "Złóż zamówienie")]]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", submitBtn)
        submitBtn.click()


    def create_account(self):
        self.fill_personal_data()
        self.fill_address()
        self.pick_delivery()
        self.choose_payment()

    def check_status(self):
        driver = self.driver
        driver.get("https://localhost/moje-konto")
        driver.find_element(By.XPATH,'//*[text()[contains(., "Historia i szczegóły zamówień")]]').click()

        elements = driver.find_elements(By.XPATH,'//*[text()[contains(., "Przygotowanie w toku")]]')

    def test_ui(self):
        maxProdsNum = 10
        firstCategoryProdsNum = random.randint(0,9)
        self.add_to_cart("https://localhost/3-lampy-wiszace", firstCategoryProdsNum)
        self.add_to_cart("https://localhost/4-kinkiety", maxProdsNum-firstCategoryProdsNum)
        self.remove_from_cart()
        self.create_account()
        self.check_status()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()