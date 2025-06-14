import json
from pysrc.local_cache import *

def import_from_json(json_file_path):
    json_file = None;
    with open(json_file_path, 'r') as fil:
        json_file = json.load(fil)

    name_list = []
    first_night = []
    other_night = []

    for ch in json_file:
        key = ch['name']
        
        if ch['id'] == '_meta':
            if not 'version' in ch:
            	ch['version'] = 'beta'
            save_edition_meta(ch)
            continue

        os.makedirs('data/'+key, exist_ok=True)
        name_list.append(key)
        firstni = ''
        otherni = ''
        setup = False
        reminders = []
        if 'firstNight' in ch:
            firstnio = ch['firstNight']
            if firstnio > 0:
                firstni = ch['firstNightReminder']
                first_night.append((firstnio, key))

        if 'otherNight' in ch:
            othernio = ch['otherNight']
            if othernio > 0:
                if 'otherNightReminder' in ch:
                    otherni = ch['otherNightReminder']
                    other_night.append((othernio, key))
            
        if 'reminders' in ch:
            reminders = ch['reminders']

        if 'remindersGlobal' in ch:
            remindersGlobal = ch['remindersGlobal']

        if 'setup' in ch:
            setup = ch['setup']

        reminder_ = {
            'firstNightRemind': firstni,
            'otherNightRemind': otherni,
            'remindIcons': reminders,
            'remindIconsGlobal': reminders,
            'affectSetup': setup,
        }
        save_character_reminder(key, reminder_)

        image_url = ''
        if 'image' in ch:
            image_url = ch['image']
        ability = ch['ability']
        team = ch['team']
        
        meta_ = {
            'ability': ability,
            'team': team,
            'tags': ["没有"],
            'script': '没有',
            'image': image_url
        }
        save_character_meta(key, meta_)

    first_night.sort(key=lambda x: x[0])
    other_night.sort(key=lambda x: x[0])

    # print(name_list)
    with open('config/first_night_order.txt', 'w') as f:
        for a in first_night:
            f.write(a[1]+"\n")
    with open('config/other_night_order.txt', 'w') as f:
        for a in other_night:
            f.write(a[1]+"\n")
    
    with open('config/team_name.json', 'w') as f:
        teamname = {
            "townsfolk": "镇民",
            "outsider": "外来者",
            "minion": "爪牙",
            "demon": "恶魔",
            "traveller": "旅行者",
            "fabled": "传奇角色",
            "jinxes": "相克",
            "unknown": "(unknown)"
        }
        json.dump(teamname, f, ensure_ascii=False)
