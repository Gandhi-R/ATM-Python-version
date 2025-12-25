import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

file_data="data.json"

def load_data():
    with open(file_data,"r") as file:
        data = json.load(file)

    for rekening in data:
        if "history" not in rekening:
            rekening["history"]=[]

    return data
    



def save_data(data):
    with open(file_data,"w") as file:
        return json.dump(data,file,indent=4)


    