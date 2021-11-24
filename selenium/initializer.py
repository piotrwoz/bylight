import os
import time
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

def find_email_field(driver):
  email_field = driver.find_element_by_id("email")
  return email_field

def find_password_field(driver):
  password_field = driver.find_element_by_id("passwd")
  return password_field

def insert_email(email_field):
  email_field.clear()
  email_field.send_keys("root@admin.com")
  return

def insert_password(password_field):
  password_field.clear()
  password_field.send_keys("rootadmin")
  password_field.send_keys(Keys.RETURN)
  return

def check_getting_to_page(delay):
  try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID,"subtab-AdminImport")))
    print ("Page is ready to use!")
  except TimeoutException:
    print("Loading is too long")
  return

def choose_upload_category(category):
  dropdown_choices = driver.find_element_by_name("entity")
  available_choices = Select(dropdown_choices)
  if category == "Produkty":
    value = 1
  elif category == "Kombinacje":
    value = 2
  available_choices.select_by_value(str(value))
  return available_choices
    
def delete_before_insert_new():
  yes_decision = driver.find_element_by_css_selector("[for='truncate_1']")
  driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", yes_decision)
  time.sleep(2)
  yes_decision.click()
  return

def force_id_before_insert_new():
  yes_decision = driver.find_element_by_css_selector("[for='forceIDs_1']")
  time.sleep(2)
  yes_decision.click()
  return

def turn_off_sending_email_about_insert():
  no_decision = driver.find_element_by_css_selector("[for='sendemail_0")
  time.sleep(2)
  no_decision.click()
  return

def switch_proper_columns():
  dropdown_options = driver.find_element_by_name("type_value[4]")
  available_options = Select(dropdown_options)
  available_options.select_by_value("price_tin")
  time.sleep(5)
  return

def execute_import():
  driver.find_element(By.ID,"import").click()
  WebDriverWait(driver, 15000).until(
  EC.element_to_be_clickable((By.ID, "import_close_button")))
  driver.find_element_by_id("import_close_button").click()
  return

def import_products():
  navigation_menu = driver.find_element_by_id("nav-sidebar")
  driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", navigation_menu)
  driver.find_elements_by_css_selector(".material-icons.mi-settings_applications")[0].click()
  
  try:
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, 'Importuj')))
    print ("Page is ready!")
  except TimeoutException:
    print("Loading took too much time!")
    
  driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", navigation_menu)
  driver.find_element_by_link_text("Importuj").click()
  
  choose_upload_category("Produkty")
  
  uploading_field = driver.find_element_by_name("file")
  
  driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", uploading_field)
  time.sleep(2)
  
  uploading_field.send_keys("C:\\Scraper2\\allProductsCSV.csv")
  time.sleep(4)
  
  #options before insert
  delete_before_insert_new()
  force_id_before_insert_new()
  turn_off_sending_email_about_insert()
  
  next_step_button = driver.find_element_by_name("submitImportFile")
  driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", next_step_button)
  time.sleep(2)
  next_step_button.click()
  
  driver.switch_to.alert.accept()
  
  switch_proper_columns()
  execute_import()
  
  time.sleep(5)  
  return

def import_combinations():
  choose_upload_category("Kombinacje") 
  uploading_field = driver.find_element_by_name("file")
  
  driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", uploading_field)
  time.sleep(2)
  
  uploading_field.send_keys("C:\\Scraper2\\allCombinationsCSV.csv")
  time.sleep(4)
  
  #options before insert
  delete_before_insert_new()
  turn_off_sending_email_about_insert()
  
  next_step_button = driver.find_element_by_name("submitImportFile")
  driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", next_step_button)
  time.sleep(2)
  next_step_button.click()
  
  driver.switch_to.alert.accept()
  
  execute_import()
  
  time.sleep(5)  
  
  return

def make_searching_available():
  navigation_menu = driver.find_element_by_css_selector(".nav-bar-overflow")
  driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", navigation_menu)
  preferences_option = driver.find_element(By.CSS_SELECTOR,".material-icons.mi-settings")

  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".material-icons.mi-settings")))

  preferences_option.click()
  
  driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", navigation_menu)
  
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Szukaj')))
  
  search_button = driver.find_element_by_link_text("Szukaj")
  search_button.click()
  
  rebuild_indexes_button = driver.find_element_by_link_text("Przebuduj cały indeks")
  rebuild_indexes_button.click()
  WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME,"alert-success")))
  return

###-----------------------------------------------------------------------
driver = webdriver.Chrome("C:\\chromedrivers\\win\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost/backoffice/")


email_field = find_email_field(driver)
insert_email(email_field)
password_field = find_password_field(driver)
insert_password(password_field)

check_getting_to_page(5)
import_products()
import_combinations()
make_searching_available()

driver.close()