import json
import os
from pysrc.local_cache import *

def generate_json_output(file_name):

    meta = get_edition_meta()
    meta['id'] = '_meta'

    output = [meta]

    # 获取所有文件
    data_files = load_character_list()

    first_night_order = load_first_night_order()
    other_night_order = load_other_night_order()

    # 添加每
    for data_name in data_files:

        metadata = load_character_meta(data_name)
        reminddata = load_character_reminder(data_name)

        fni = 0
        oni = 0
        fnirem = ""
        onirem = ""
        if data_name in first_night_order:
            fni = first_night_order.index(data_name)+1
            fnirem = reminddata['firstNightRemind']
        if data_name in other_night_order:
            oni = other_night_order.index(data_name)
            onirem = reminddata['otherNightRemind']
        
        output.append({
            'id': str(data_name.__hash__()),
            'image': metadata['image'],
            'edition': 'custom',
            'name': data_name,
            'ability': metadata['ability'],
            'team': metadata['team'],
            'firstNight': fni,
            'otherNight': oni,
            'firstNightReminder': fnirem,
            'otherNightReminder': onirem,
            'reminders': reminddata['remindIcons'],
            'remindersGlobal': reminddata['remindIconsGlobal'],
            'setup': reminddata['affectSetup']
        })

    with open(f'output/{file_name}.json', 'w') as f:
        json.dump(output,f, ensure_ascii=False)