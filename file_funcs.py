import os 
import json

def user_datas() -> dict:
    with open("datas/datas.json","r+",encoding="utf-8") as file:
        return json.load(file)

def user_saving(follows:dict = None,followers:dict = None) -> dict:
    if followers == None and follows == None:
        with open("datas/users.json","r+",encoding="utf-8") as file:
            datas:dict = json.load(file)
        return datas

    with open("datas/users.json","r+", encoding="utf-8") as file:
        datas:dict = json.load(file)

    if followers == None:
        with open("datas/users.json","w", encoding="utf-8") as file:
            datas["follows"] = follows
            json.dump(datas,file,sort_keys=False,indent=4)
    
    elif follows == None:
        with open("datas/users.json","w", encoding="utf-8") as file:
            datas["followers"] = followers
            json.dump(datas,file,sort_keys=False,indent=4)
    

