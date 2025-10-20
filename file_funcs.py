import os 
import json

def user_datas():
    with open("datas/datas.json", "r+" , encoding="utf-8") as file:
        datas:dict = json.load(file)
    return datas

class follow_file:
    def __int__(self):
        self.file_creater()

    def file_creater(self):
        with open("datas/users.json","a",encoding="utf-8") as file:
            pass
    
    

