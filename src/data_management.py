# CB 1st Final Project Data Management

import csv

# def load_game(file_path):
    # use with open to load file and close it when finished
    # load all neccesary data


# def save_game(file_path):
    # use with open to save file and close it when finished
    # save al neccesary data (base stats, upgrades, meta currency)

def load_game(file_path):
    with open(file_path, mode="r", newline="") as user_csv:
        fieldnames = ["max_health","damage_mod","i_frame_mod","money","upgrades"]
        reader = csv.DictReader(user_csv, fieldnames=fieldnames)
        
        # 1. Skip the header row
        next(reader) 
        
        # 2. Grab the actual data row
        data = next(reader)
    upgrades=[]
    with open(data['upgrades'],mode="r",newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            upgrades=row
    user_data=data
    user_data['upgrades']=upgrades
    print(user_data)
    return user_data

def save_game(file_path,user_data):
    if file_path=='documents/savefile_one.csv':
        with open('documents/one_upgrades.csv',mode="w",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(user_data["upgrades"])
    with open(file_path,mode="w",newline="") as user_csv:
        fieldnames = ["max_health","damage_mod","i_frame_mod","money","upgrades"]
        writer = csv.DictWriter(user_csv,fieldnames)
        save_data=user_data
        if file_path=='documents/savefile_one.csv': save_data["upgrades"]='documents/one_upgrades.csv'
        top_row={}
        for i in fieldnames: top_row[i]=i
        writer.writerow(top_row)
        writer.writerow(save_data)
    

load_game('documents/savefile_one.csv')
save_game('documents/savefile_one.csv',{'max_health': '5.0', 'damage_mod': '1.0', 'i_frame_mod': '1.0', 'money': '200', 'upgrades': ['+1 HEALTH', '+1 HEALTH 2']})