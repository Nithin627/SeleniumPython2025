import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# import pdb

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demostore.supersqa.com/")
time.sleep(2)

# cart = driver.find_element(By.ID,'site-header-cart')
# cart.click()

driver.get("http://demostore.supersqa.com/my-account/")
# pdb.set_trace()
time.sleep(2)
driver.execute_script("window.scrollBy(0,300)")
time.sleep(2)
# Using xpath
u_name=driver.find_element(By.XPATH,"//input[@name='username']")
u_name.send_keys("Nithin")





