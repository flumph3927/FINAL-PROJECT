# CB 1st Final Project Data Management

import csv

# def load_game(file_path):
    # use with open to load file and close it when finished
    # load all neccesary data


# def save_game(file_path):
    # use with open to save file and close it when finished
    # save al neccesary data (base stats, upgrades, meta currency)

def load_game(file_path):
    with open(file_path,mode="r",newline="") as user_csv:
        fieldnames = ["health_mod","damage_mod","i_frame_mod","weapons","upgrades","meta_currency"]

        reader = csv.DictReader(user_csv,fieldnames)

        user_data = {}

        for i in reader:
            user_data.append(i)

    return user_data

def save_game(file_path,user_data):
    with open(file_path,mode="w",newline="") as user_csv:
        fieldnames = ["health_mod","damage_mod","i_frame_mod","weapons","upgrades","meta_currency"] # figure this out later

        writer = csv.DictWriter(user_csv,fieldnames)

        for i in user_data:
            writer.writerow(i)