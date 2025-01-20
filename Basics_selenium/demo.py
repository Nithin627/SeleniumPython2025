import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# driver=webdriver.Chrome(execute_path='/driver/chromedriver')
# driver=webdriver.Edge()
# se=Service(execute_path='/driver/chromedriver')
# driver=webdriver.chrome(service=se)

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

# go to url
driver.get("http://demostore.supersqa.com/")
time.sleep(3)

# click on my acccount
# driver.find_element_by_link_text('My account').click()
account=driver.find_element(By.LINK_TEXT,'My account')
account.click()
# driver.find_element(By.XPATH("(//div[@class='menu']/ul/li[4])[1]")).click()
time.sleep(3)

# scroll
driver.execute_script("window.scrollBy(0,300)")
username="Nithin"
password="1234"
uname=driver.find_element(By.ID,"username")
uname.send_keys(username)
Pass=driver.find_element(By.ID,"password")
Pass.send_keys(password)

# click
driver.find_element(By.NAME,"login").click()
time.sleep(3)

error_list_elm= driver.find_elements(By.CSS_SELECTOR,'ul.woocommerce-error li')
first_error_elm=error_list_elm[0]
displayed_error_text = first_error_elm.text

# verify
expected_error=f"Error: The username {username} is not registered on this site. If you are unsure of your username, try your email address instead."
assert expected_error==displayed_error_text, "Displayed error is not as expected."
print("Success...")

driver.quit()