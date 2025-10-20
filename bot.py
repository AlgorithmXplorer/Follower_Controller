
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import time

class Bot:

    def __init__(self,username:str ,password:str):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome(options=self.driver_maker())
        self.driver.maximize_window()

    def driver_maker(self) -> Options:
        options = Options()
        options.add_argument("--lang=en-US")
        # options.add_argument("--headless")
        options.add_argument("--incognito")
        
        return options
    
    def log_in(self):
        self.driver.get(url= "https://github.com/login")

        username_inp = self.driver.find_element(By.CSS_SELECTOR , "#login_field")
        username_inp.send_keys(self.username)
        time.sleep(3.5)

        psw_inp = self.driver.find_element(By.CSS_SELECTOR , "#password")
        psw_inp.send_keys(self.password)
        psw_inp.send_keys(Keys.ENTER)





