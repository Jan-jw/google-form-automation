from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#simple login to webpage and confirm loginPage title

browser = webdriver.Chrome() # instantiate chrome browser
browser.get("https://opensource-demo.orangehrmlive.com/") # load the page with a URL

try:
    # makes sure page DOM loaded
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))

    )

    uName = browser.find_element(By.NAME, "username").send_keys("Admin")
    pWord = browser.find_element(By.NAME, "password").send_keys("admin123")
    submitBtn = browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

    if browser.title == "OrangeHRM":
        print("test success")
    else:
        print("test failed")
finally:
    print(browser.title)
    browser.close()
