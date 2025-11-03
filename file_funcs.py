import time
import json

def user_datas() -> dict:
    """
    Return gmail app_pasw gml_pasw and userame 
    """
    for i in range(10):
        try:
            with open("datas/datas.json","r+",encoding="utf-8") as file:
                return json.load(file)
        except:
            time.sleep(5)
        else:
            break


def user_saving(follows:dict = None,followers:dict = None) -> dict:
    """
    Return follower and follows or saving them 
    """
    for i in range(10):
        try:    
            if followers is None and follows is None:
                with open("datas/users.json","r+",encoding="utf-8") as file:
                    datas:dict = json.load(file)
                return datas

            with open("datas/users.json","r+", encoding="utf-8") as file:
                datas:dict = json.load(file)

            if followers is None and follows is not None:
                with open("datas/users.json","w", encoding="utf-8") as file:
                    datas["follows"] = follows
                    json.dump(datas,file,sort_keys=False,indent=4)

            elif follows is None and followers is not None:
                with open("datas/users.json","w", encoding="utf-8") as file:
                    datas["followers"] = followers
                    json.dump(datas,file,sort_keys=False,indent=4)
        except:
            time.sleep(5)
        else:
            break