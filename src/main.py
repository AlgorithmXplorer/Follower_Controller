
from src.bot import Bot
from src.file_funcs import user_saving,user_datas
from src.mail_funcs import Mailer,mail_reader
from src.timer import timer
import time

import pandas as pd


class Main:
    def __init__(self,datas:dict):
        self.datas = datas
        self.bot = Bot(datas=self.datas)

        self.bot.log_in(mail_reader=mail_reader)
        time.sleep(2)        


    def main(self):
        while True:
            self.bot.driver.get(self.bot.main_url)

            self.follower_cont()
            time.sleep(5)
            self.follow_cont()
            wait_time = timer()
            time.sleep(wait_time)



    def follower_cont(self):
        there_are_followers = user_saving()["followers"] 
        if there_are_followers == {}:
            user_saving(followers=self.bot.follower_taker()) 
        
        old_followers = user_saving()["followers"]

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
        follows_list = self.bot.following_taker()
        user_saving(follows=follows_list)

        follows_dict = {"names":list(follows_list.keys()), "links":list(follows_list.values())} 
        df_follow = pd.DataFrame(data=follows_dict)

        follower_list = list(user_saving()["followers"].keys())

        unfollowers = df_follow[df_follow["names"].apply(func=lambda name: name not in follower_list)]
        
        if len(unfollowers.index) != 0:
            after_fiter = self.bot.profile_filter(users=unfollowers)
            will_unflw = after_fiter[0]
            will_stay_flw = after_fiter[1]

            stay_follow_df = df_follow[df_follow["names"].apply(func=lambda name: name in follower_list)]
            for name,link in zip(stay_follow_df["names"],stay_follow_df["links"]):
                will_stay_flw.update({name:link})

            user_saving(follows=will_stay_flw)

            unflw_df = pd.DataFrame(data= {"names":list(will_unflw.keys()),"links":list(will_unflw.values())})
            self.bot.unfollow(users=unflw_df)
    
        
datas = user_datas()
x = Main(datas=datas)
x.main()


