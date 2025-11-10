
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

class Bot:

    def __init__(self,datas:dict):
        self.datas = datas
        self.username = self.datas["username"]
        self.password = self.datas["password"]
        self.app_password = self.datas["app_password"]
        self.gmail = self.datas["gmail"]

        self.main_url = "https://github.com/" 

        self.driver = webdriver.Chrome(options = self.driver_maker())
        self.driver.maximize_window()

    def driver_maker(self) -> Options:
        options = Options()
        options.add_argument("--lang=en-US")
        options.add_argument("--headless")
        # options.add_argument("--incognito")
        
        return options
    
    def log_in(self,mail_reader):
        self.driver.get(url= self.main_url+"login")
        time.sleep(2)

        username_inp = self.driver.find_element(By.CSS_SELECTOR , "#login_field")
        username_inp.send_keys(self.username)
        time.sleep(3.5)

        psw_inp = self.driver.find_element(By.CSS_SELECTOR , "#password")
        psw_inp.send_keys(self.password)
        time.sleep(1)
        psw_inp.send_keys(Keys.ENTER)
        time.sleep(3)

        try:
            is_verifaction = self.driver.find_element(By.XPATH,"//*[@id='login']/div[4]/div/ul/li/a")
            is_verifaction.click()
            time.sleep(7.5)

            datas = mail_reader(self.gmail,self.app_password)
            code_inp_tag = self.driver.find_element(By.CSS_SELECTOR , "#otp")
            code_inp_tag.send_keys(datas)
            time.sleep(1)
            code_inp_tag.send_keys(Keys.ENTER)
            time.sleep(3)

        except:
            self.driver.get(url=self.main_url)
            


    def following_taker(self) -> dict:
        self.driver.get(url=self.main_url + self.username )
        time.sleep(5)

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
            
            except :
                break

        return followers

    
    def unfollow(self,users):
        self.driver.get(url= self.main_url)
        time.sleep(2)

        urls_list = users["links"]
        
        def unfllw(url):
            self.driver.get(url=url)
            time.sleep(2)

            unflw_tag = self.driver.find_element(By.XPATH,"//input[@data-disable-with='Unfollow']")
            unflw_tag.click()
            time.sleep(2)


        for url in urls_list:
            unfllw(url=url)            

        

    def mail_information(self,users) -> str:
        self.driver.get(url=self.main_url)
        time.sleep(2)

        urls_list = users["links"]

        infos = []

        def info_taker(url:str):
            self.driver.get(url=url)

            username = self.driver.find_element(By.XPATH , "//span[@itemprop='additionalName']").text
            follower_count = self.driver.find_element(By.CSS_SELECTOR , ".text-bold.color-fg-default").text 

            message = f"""<h3 style="color: red;"><b>{username}</b> Followed You!</h3><ul style="font-size: 16px;"><br><li style="color: blue;"><b>Link:</b> {url}.</li><br><li style="color: green;"><b>Follower Count:</b> {follower_count}.</li><br></ul>
"""
            return message

        for url in urls_list:
            try:
                msg = info_taker(url=url)
                infos.append(msg)
                time.sleep(1.5)
            except:
                continue
            
        all_msg = f"<h1>{'-'*45}</h1>".join(infos)
        return all_msg

 
    def profile_filter(self,users) -> list[dict]:
        self.driver.get(self.main_url)
        time.sleep(2)
        links = list(users["links"])


        will_unfollow = {}
        will_stay_follow = {}
        for link in links:
            self.driver.get(url=link)
            time.sleep(0.5)
            tags = self.driver.find_elements(By.CSS_SELECTOR , ".text-bold.color-fg-default")
            counts = [float(tag.text[:-1])*1000 if "k" in tag.text else int(tag.text) for tag in tags]
            follower_count = counts[0]
            following_count = counts[1]

            user_name = link.split("/")[-1]

            if follower_count <= 500:
                will_unfollow.update({user_name:link})
            elif follower_count + following_count < 1000:
                will_unfollow.update({user_name:link})
            else:
                will_stay_follow.update({user_name:link})
                time.sleep(0.5)
                

        return [will_unfollow , will_stay_follow]


    def closer(self):
        self.driver.close()

