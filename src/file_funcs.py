import time
import json

path = "the path of folder that contains data json files"


# This function reads and returns the user information used across methods and functions
# from the "datas.json" file.
# If it fails to fetch the necessary data, the bot cannot operate. For instance, without the username
# or password, the login process cannot proceed and the program will crash.
def user_datas() -> dict:
    """
    Return gmail app_pasw gml_pasw and userame 
    """
    # A loop is used so that it doesn’t throw an immediate error if it cannot access
    # the data files (the JSON files).
    # If you start the application without adding the data files, you will have some time to fix it.
    for i in range(10):
        try:
            with open(path + "/datas.json","r+",encoding="utf-8") as file:
                data = json.load(file)
        except:
            time.sleep(5)
        else:
            return data
            

    # The purpose of this function is to ensure that old follower and following data
    # is updated during the hourly checks.
def user_saving(follows:dict = None,followers:dict = None) -> dict:
    """
    Return follower and follows or saving them 
    """

    if followers is None and follows is None:
        # A loop is used so that it doesn’t throw an immediate error if it cannot access
        # the data files (the JSON files).
        # If you start the application without adding the data files, you will have some time to fix it.
        for i in range(10):
            try:
                with open(path + "/users.json","r+",encoding="utf-8") as file:
                    datas:dict = json.load(file)
                return datas
            except:
                time.sleep(5)


        # A loop is used so that it doesn’t throw an immediate error if it cannot access
        # the data files (the JSON files).
        # If you start the application without adding the data files, you will have some time to fix it.
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

