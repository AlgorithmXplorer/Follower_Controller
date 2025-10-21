
from bot import Bot
from file_funcs import *

import time
import json

datas = user_datas()
username = datas["username"]
password= datas["password"]


x = user_saving()
print(x)

x = Bot(username=username,password=password)
x.log_in()

users = x.following_taker()

users_1 = x.follower_taker()


# time.sleep(1000)

user_saving(followers=users_1)
user_saving(follows=users)
x = user_saving()
print(x)

