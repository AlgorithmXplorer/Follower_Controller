
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

        self.main_url = "https://github.com/" 

        self.driver = webdriver.Chrome(options=self.driver_maker())
        self.driver.maximize_window()

    def driver_maker(self) -> Options:
        options = Options()
        options.add_argument("--lang=en-US")
        # options.add_argument("--headless")
        options.add_argument("--incognito")
        
        return options
    
    def log_in(self):
        self.driver.get(url= self.main_url+"login")
        time.sleep(2)

        username_inp = self.driver.find_element(By.CSS_SELECTOR , "#login_field")
        username_inp.send_keys(self.username)
        time.sleep(3.5)

        psw_inp = self.driver.find_element(By.CSS_SELECTOR , "#password")
        psw_inp.send_keys(self.password)
        psw_inp.send_keys(Keys.ENTER)
        time.sleep(2)


    def following_taker(self) -> dict:
        self.driver.get(url=self.main_url + self.username )
        time.sleep(2)

        follow_tag = self.driver.find_element(By.XPATH , "/html/body/div[1]/div[6]/main/div/div/div[1]/div/div/div[3]/div[2]/div[3]/div/a[2]")
        follow_tag.click()
        time.sleep(2)

        def user_taker():
            xpath = ["//*[@id='user-profile-frame']/div/div[" , "1" , "]/div[2]/a"]

            clear_users = {}

            while True:
                try:
                    new_xpath = "".join(xpath)

                    a_tag = self.driver.find_element(By.XPATH , new_xpath )
                    
                    link = a_tag.get_attribute("href")
                    username = a_tag.find_element(By.XPATH , new_xpath + "/span[2]").text
                    
                    clear_users.update({username:link})

                    xpath[1] = str(int(xpath[1]) + 1)

                except:
                    break

            return clear_users
        
        users = {}
        while True:
            try:
                taken_users = user_taker()
                users.update(taken_users)
                time.sleep(2)

                next_tag = self.driver.find_elements(By.XPATH , "//a[@rel='nofollow']")
                true_next = [tag for tag in next_tag if tag.text =="Next"]
                true_next[0].click()
                time.sleep(3)

            except:
                break
        return users

    #t NOT: YAGMAİL İLE YAPICAĞIMIZ FONKSYİON İÇİN AYRI BİR FONKSİYON YAPICAZ. BU FUNC BİZE TAKİPÇİLERİ KAYDEDECEĞİMİZ
    #T      DOSYADAKİ TAKİPÇİlERİ ÇIKTI EDİCEK VE FOLLOW_TAKER DAN ÖNCE VE SONRA ÇALIŞICAK ARDINDAN ALINAN İKİ LİSTE İLE(KEY LİSTESİ) BİZDE YAGMAİL FONKSİYONU İÇİNDE FARKLI OLANLARI BULUP YAGMAİL İLE ÇIKTI EDİCEZ.
    #T      BU FONKSİYON İLE TAKİP ETMEYİ BIRAKANLARIDA BULABİLİRİZ  


    def follower_taker(self) ->dict :
        self.driver.get(url=self.main_url + self.username)
        time.sleep(3)

        follwer_tag = self.driver.find_element(By.XPATH , "/html/body/div[1]/div[6]/main/div/div/div[1]/div/div/div[3]/div[2]/div[3]/div/a[1]")
        follwer_tag.click()
        time.sleep(3)

        def user_taker():
            user_tags = self.driver.find_elements(By.XPATH , "//a[@class='d-inline-block no-underline mb-1']" )
            users = {}
            for tag in user_tags:
                link = tag.get_attribute("href")
                name = tag.get_attribute("href").split("/")[-1]
                users.update({name:link})
                 
            return users
        
        followers = {}
        
        while True:
            try:
                followers.update(user_taker())

                next_tag = self.driver.find_elements(By.XPATH , "//a[@rel='nofollow']")
                next_tag = [tag for tag  in next_tag if tag.text == "Next"][0]
                
                next_tag.click()
                time.sleep(3)
            
            except Exception as error:
                break

        return followers

    def controller(self):
        pass
        #* takip edilenleri belirlediğimiz kıraterde olmayanları alıp çıktı edicek

    
    def unfollow(self,urls:dict):
        pass

    def mail_information(self,urls) -> str:
        pass
    #* aldığı hesapların takipçi ile takip sayısını alıp şu şekil çıktı vericek
    """
    -----
    xxx hesabı 
    takipçi: 
    url:
    -----
    """

    def closer(self):
        self.driver.close()

