
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

    # Infinite loop method that ensures operations run at the start of every hour
    def main(self):
        time.sleep(30)
        while True:
            self.bot.driver.get(self.bot.main_url)

            self.follower_cont()
            time.sleep(5)
            self.follow_cont()
            wait_time = timer()
            time.sleep(wait_time)


    # This method contains all follower-related operations. It combines them all together
    def follower_cont(self):
    
        # First, it retrieves the follower data from the saved file 
        are_there_followers = user_saving()["followers"] 

        # If no data exists, the bot will first save follower data. This is for the first run or when data is deleted.
        if are_there_followers == {}:
            user_saving(followers=self.bot.follower_taker()) 
        
        # Retrieve the old list of followers. This is needed to compare with the new list.
        old_followers = user_saving()["followers"]
        old_names = list(old_followers.keys()) 
        
        # Retrieve current followers from the profile using the bot and convert to DataFrame
        new_follower_list = self.bot.follower_taker()
        new_dict = {"names":list(new_follower_list.keys()) , "links":list(new_follower_list.values())}
        new_df = pd.DataFrame(data=new_dict) 
        
        # Using apply(), get users who are in the new list but not in the old list → these are new followers.
        new_followers = new_df[new_df["names"].apply(func= lambda str_data: str_data not in old_names)]
        
        # If there are new followers, update the list and send them via email as a message.
        if len(new_followers.index) != 0:
            msg = self.bot.mail_information(new_followers)

            Mailer(app_psw=self.datas["app_password"],gmail=self.datas["gmail"],datas=msg)
            user_saving(followers=new_follower_list)


    # This method contains all follow-related operations. It combines them all together
    def follow_cont(self):

        # Retrieve the following list and save it because it will be compared with the follower list
        follows_list = self.bot.following_taker()
        user_saving(follows=follows_list)

        # Convert the following list into a DataFrame
        follows_dict = {"names":list(follows_list.keys()), "links":list(follows_list.values())} 
        df_follow = pd.DataFrame(data=follows_dict)

        # Compare following list with follower list to find users who do not follow you back
        follower_list = list(user_saving()["followers"].keys())
        unfollowers = df_follow[df_follow["names"].apply(func=lambda name: name not in follower_list)]
        
        # Pass non-followers through the profile filter and unfollow unnecessary accounts
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


