from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

class Form(webdriver.Firefox): # inherit chrome webdriver broswer object
    def __init__(self, formURL): # load the form
        self.formURL = formURL


        profile = webdriver.FirefoxProfile("/Users/jw/Library/Application Support/Firefox/Profiles/sasjnuvg.default-release")

        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference('useAutomationExtension', False)
        profile.update_preferences()
        desired = DesiredCapabilities.FIREFOX

        super(Form, self).__init__(firefox_profile=profile,
                           desired_capabilities=desired)
         # self is basically the chrome browser object
        # self.maximize_window()
        self.get(self.formURL)
        self.implicitly_wait(25)
        #
        # # login
        # self.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("janicew2177@gmail.com")
        # self.find_element(By.TAG_NAME, "button").click()
        # clear_btn = self.find_element(By.XPATH, "//*[contains(text(), 'Clear form')]")
        # clear_btn.click()
        # try:
        #     element = WebDriverWait(self, 15).until(
        #         EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Clear form')]"))
        #     )
        # finally:
        #     clear_btn = self.find_element(By.XPATH, "//*[contains(text(), 'Clear form')]")
        #     # ActionChains(self).move_to_element(clear_btn).click().perform()
        #     # clear_btn.click()
        #     self.execute_script("arguments[0].click();", clear_btn)

        self.form = self.find_element(By.CSS_SELECTOR, "form[method='POST']")
        self.listNum = int(self.form.get_attribute("data-last-entry"))
        # self.inputList = self.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
        self.inputList = self.find_elements(By.CSS_SELECTOR, "div[class='Qr7Oae']")
    def __exit__(self):
        pass
        self.close()

    def clearForm(self):
        self.find_element(By.XPATH, "//*[contains(text(), 'Clear form')]").click()

    def input_shorttext(self, boxEle, value):
        print(boxEle.text)
        # boxEle.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(value)# the input text should be placed
        boxEle.find_element(By.TAG_NAME, "input").send_keys(value)# the input text should be placed

    def input_textarea(self, boxEle, value):
        boxEle.find_element(By.TAG_NAME, "textarea").send_keys(value)

    def select_mc(self, boxEle, name):
        boxEle.find_element(By.CSS_SELECTOR, f"div[data-value='{name}']").click()
        # catch exceptiption
        # self.boxEle.getElement(By.CSS_SELECTOR, "div[role='radio']")

    def select_checkbox(self, boxEle, name):
        print(boxEle.text)
        boxEle.find_element(By.CSS_SELECTOR, f"div[data-answer-value='{name}']").click()
        # other option : input text box

    def dropdown(self, boxEle, name):
        print(boxEle.text)
        WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='presentation']"))
            ).click()
        WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@class='OA0qNb ncFHed QXL7Te']//div[@data-value='{name}']"))
        ).click()

    # def file_upload(self):

    def linear_scale(self, boxEle, value):
        boxEle.find_element(By.CSS_SELECTOR, f"div[data-value='{value}']").click()

    def mc_grid(self, value_list):
        # value_list = [(name,idx)]
        for (name,pos) in value_list:
            print(name)
            row = WebDriverWait(self, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, f"//div[text()='{name}']/following-sibling::div[@class='V4d7Ke']/div/div[@role='radio']"))
            )
            row[pos].click()

    def checkbox_grid(self, value_list):
        # value_list = {key:(), key2:()}
        for name, pos in value_list.items():
            # row = WebDriverWait(self, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, f"//div[text()='{name}']/following-sibling::div[@class='V4d7Ke']/div[@role='checkbox']"))
            # )
            # row = boxEle.find_elements(By.XPATH, f"//div[text()='{name}']/following-sibling::div[@class='V4d7Ke']/div[@role='checkbox']")
            # row.location_once_scrolled_into_view
            print(pos)
            for i in pos:
                row = WebDriverWait(self, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, f"//div[text()='{name}']/following-sibling::label[@class='V4d7Ke']//div[@role='checkbox' and @data-answer-value='{i}']"))
                    ).click()
                # row[i].location_once_scrolled_into_view


    def input_date(self, boxEle, date): # shows cross broswer test is needed
        # date : mmddyyyy
        # div class="Xb9hP"
        # input aria-label="Month"
        # class="Xb9hP"
        # aria-label="Day of the month"
        # class="a7KROc uTyfEf"
        # aria-label="Year"
        # self.switch_to.frame(self.find_element_by_tag_name('iframe'))
        print(boxEle.text)
        date_list = date.split('-')
        # dateb = boxEle.find_element(By.CSS_SELECTOR, "div[class='o7cIKf']")
        month = WebDriverWait(boxEle, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[aria-label='Month']"))
        ).send_keys(date_list[1])

        day = WebDriverWait(boxEle, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[aria-label='Day of the month']"))
        ).send_keys(date_list[2])

        year = WebDriverWait(boxEle, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[aria-label='Year']"))
        ).send_keys(date_list[0])


        # print(date.text)
        # dateb.send_keys(date)
        # self.switch_to.default_content()

    def input_time(self, boxEle, time, period):
        #time-> 12:12
        # aria-label="Hour"
        # aria-label="Minute"

        # div
        # data-value="PM"
        #  role="option"
        # class="MocG8c HZ3kWc mhLiyf LMgvRb"
        time = time.split(':')
        boxEle.find_element(By.CSS_SELECTOR, "input[aria-label='Hour']").send_keys(time[0])
        boxEle.find_element(By.CSS_SELECTOR, "input[aria-label='Minute']").send_keys(time[1])

        if period != "AM":
            WebDriverWait(boxEle, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "div[role='presentation']"))
            ).click()
            WebDriverWait(self, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='OA0qNb ncFHed QXL7Te']//div[@data-value='PM']"))
            ).click()


    def submit(self):
        self.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click()