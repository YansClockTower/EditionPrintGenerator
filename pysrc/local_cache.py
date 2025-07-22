import json
import os

##########################################
# Configs

config_file = 'config/team_name.json'
first_night_order_file = 'config/first_night_order.txt'
other_night_order_file = 'config/other_night_order.txt'

def load_team_map():
    with open(config_file, "r") as f:
        return json.load(f)

def load_first_night_order():
    with open(first_night_order_file, 'r') as f:
        lines = [line.strip() for line in f]
        return lines

def load_other_night_order():
    with open(other_night_order_file, 'r') as f:
        lines = [line.strip() for line in f]
        return lines

def save_team_map(d):
    with open(config_file, "w") as f:
        json.dump(d, f)

def save_first_night_order(d):
    with open(first_night_order_file, 'w') as f:
        for i in d:
            first_night_order_file.write(i+'\n')

def save_other_night_order(d):
    with open(other_night_order_file, 'w') as f:
        for i in d:
            other_night_order_file.write(i+'\n')

#############################################
# Characters

data_dir = 'data'

def load_character_list():
    return sorted(os.listdir(data_dir), key=lambda x: x.lower())

def load_character_meta(name):
    data_path = os.path.join(data_dir, name).replace("\\", "/")  # 兼容 Windows 路径
    metadata_path = os.path.join(data_path, 'meta.json').replace("\\", "/")

    with open(metadata_path, "r") as f:
        return json.load(f)
    
def load_character_reminder(name):
    data_path = os.path.join(data_dir, name).replace("\\", "/")  # 兼容 Windows 路径
    remind_path = os.path.join(data_path, 'remind.json').replace("\\", "/")
    
    with open(remind_path, "r") as f:
        return json.load(f)
    
def save_character_meta(name, data):
    data_path = os.path.join(data_dir, name).replace("\\", "/")  # 兼容 Windows 路径
    metadata_path = os.path.join(data_path, 'meta.json').replace("\\", "/")

    with open(metadata_path, "w") as f:
        json.dump(data, f, ensure_ascii=False)
    
def save_character_reminder(name, data):
    data_path = os.path.join(data_dir, name).replace("\\", "/")  # 兼容 Windows 路径
    remind_path = os.path.join(data_path, 'remind.json').replace("\\", "/")
    
    with open(remind_path, "w") as f:
        json.dump(data, f, ensure_ascii=False)


#############################################
# edition meta

config_dir = 'config'

def get_edition_meta():
    data_path = os.path.join(config_dir, "edition_meta.json").replace("\\", "/")  # 兼容 Windows 路径
    with open(data_path, "r") as f:
        return json.load(f)

def save_edition_meta(data):
    data_path = os.path.join(config_dir, "edition_meta.json").replace("\\", "/")  # 兼容 Windows 路径
   
    with open(data_path, "w") as f:
        json.dump(data, f, ensure_ascii=False)

def get_statement():
    data_path = os.path.join(config_dir, "statement.json").replace("\\", "/")  # 兼容 Windows 路径
    if os.path.exists(data_path):
        with open(data_path, "r") as f:
            return json.load(f)

def save_statement(data):
    data_path = os.path.join(config_dir, "statement.json").replace("\\", "/")  # 兼容 Windows 路径
   
    with open(data_path, "w") as f:
        json.dump(data, f, ensure_ascii=False)
