import json

file_data="data.json"

def load_data():
    with open(file_data,"r") as file:
        return json.load(file)


def save_data(data):
    with open(file_data,"w") as file:
        return json.dump(data,file,indent=4)


    