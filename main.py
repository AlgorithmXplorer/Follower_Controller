
from bot import Bot
from file_funcs import *
import time
import json


#* datas
datas = user_datas()
username = datas["username"]
password= datas["password"]
gmail = datas["gmail"]
app_pasw = datas["app_password"]


bot = Bot(username=username,password=password)
bot.log_in()
all_users:dict = user_saving()

# follows = bot.following_taker()

# followers = bot.follower_taker()

links = list(all_users["follows"].values())[:5]

# bot.unfollow(urls=links)


time.sleep(1000)

# user_saving(followers=followers)
# user_saving(follows=follows)




