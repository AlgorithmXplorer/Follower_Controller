import time
import json

path = "the path of folder that contains data json files"

def user_datas() -> dict:
    """
    Return gmail app_pasw gml_pasw and userame 
    """
    for i in range(10):
        try:
            with open(path + "/datas.json","r+",encoding="utf-8") as file:
                data = json.load(file)
        except:
            time.sleep(5)
        else:
            return data
            


def user_saving(follows:dict = None,followers:dict = None) -> dict:
    """
    Return follower and follows or saving them 
    """

    if followers is None and follows is None:
        for i in range(10):
            try:
                with open(path + "/users.json","r+",encoding="utf-8") as file:
                    datas:dict = json.load(file)
                return datas
            except:
                time.sleep(5)


    for i in range(10):
        try:    
            with open(path + "/users.json","r+", encoding="utf-8") as file:
                datas:dict = json.load(file)

            if followers is None and follows is not None:
                with open(path + "/users.json","w", encoding="utf-8") as file:
                    datas["follows"] = follows
                    json.dump(datas,file,sort_keys=False,indent=4)

            elif follows is None and followers is not None:
                with open(path + "/users.json","w", encoding="utf-8") as file:
                    datas["followers"] = followers
                    json.dump(datas,file,sort_keys=False,indent=4)

        except:
            time.sleep(5)
            
        else:
            break

