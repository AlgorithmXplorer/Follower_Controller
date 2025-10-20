
from bot import Bot
import time
import json

with open("datas/datas.json","r+",encoding="utf-8") as file:
    datas:dict = json.load(file)
    username = datas["username"]
    password = datas["password"]


x = Bot(username=username,password=password)
x.log_in()
time.sleep(1000)


