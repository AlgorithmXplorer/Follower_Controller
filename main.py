
from bot import Bot
from file_funcs import *
from mailer import *
from timer import *
import time
import json
import pandas as pd


class Main:
    def __init__(self,datas:dict, ):
        self.datas = datas
        self.bot = Bot(username=self.datas["username"],password=self.datas["password"])

        self.bot.log_in()

    def follower_cont(self):
        old_followers = user_saving()["followers"]
        if old_followers == {}:
            user_saving(followers=self.bot.follower_taker()) 

        old_names = list(old_followers.keys()) 
        
        new_follower_list = self.bot.follower_taker()
        new_dict = {"names":list(new_follower_list.keys()) , "links":list(new_follower_list.values())}
        new_df = pd.DataFrame(data=new_dict) 
        
        new_followers = new_df[new_df["names"].apply(func= lambda str_data: str_data not in old_names)]
        if len(new_followers.index) != 0:
            msg = self.bot.mail_information(new_followers)

            Mailer(app_psw=self.datas["app_password"],gmail=self.datas["gmail"],datas=msg)
            user_saving(followers=new_follower_list)

    def follow_cont(self):
        pass


datas = user_datas()

x = Main(datas=datas)
x.follower_cont()
