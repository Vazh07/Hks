import os 
import json 
import random

def mix(poems):
    maxV = 3
    maxP = len(poems)
    poem = ''
    for i in range(maxV):
        rV = random.randint(0, maxV - 1)
        rP = random.randint(0, maxP - 1)
        poem += poems[rP][rV] + " / "
    yield poem

def readHaikus(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        file_list = os.listdir(folder_path)
        json_files = [file for file in file_list if file.endswith('.json')]
        APP=[] #All Poems Parts
        for json_file in json_files:
            file_path = os.path.join(folder_path, json_file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                poems = data["content"].get("poems","No poems were found!!!")
                p_parts = [list(poem.values())[0].split('/') for indx, poem in enumerate(poems)]
                APP+=p_parts
        return APP
    else:
        raise Exception(f"The folder '{folder_path}' does not exist or is not a directory.")

def executeMain():
    path = "../../data"
    try: 
        poems = readHaikus(path)
        for poem in mix(poems):
            print(poem)
    except Exception as e:
        print(f"An exception occurred at executeMain: {e}")
    else:
        print("End of program")

if __name__=='__main__':
    pass
    #executeMain()