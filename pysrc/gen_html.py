import os
import json
from pysrc.local_cache import *
import datetime

REMOTE = True

def sort_func(x):
        if x.startswith('towns'):
            return 1
        if x.startswith('outsid'):
            return 2
        if x.startswith('minion'):
            return 3
        if x.startswith('demon'):
            return 4
        if x.startswith('travel'):
            return 5
        if x.startswith('fable'):
            return 6
        return 7

def load_html_file(filename,config):
    with open(filename, "r", encoding="utf-8") as f:
        htmldata += f.read()
        #for dkey in config:
        #    htmldata = htmldata.replace(f"%%{dkey}%%",config[dkey])
        return htmldata

def generate_html_output(file_name):
    meta = get_edition_meta()

    EDITION_NAME = meta['name']
    VERSION = meta['version']
    AUTHOR = meta['author']
    

    root_dir = 'data'
    # 获取所有文件
    data_files = load_character_list()

    team_map = {}
    datas = []
    with open("config/team_name.json", "r") as f:
        team_map = json.load(f)
        
    #with open("global_config.json", "r") as f:
    #    team_map = json.load(f)
        
    # 添加每张图片到 HTML 中
    for data_name in data_files:
        data_path = os.path.join(root_dir, data_name).replace("\\", "/")  # 兼容 Windows 路径
        icon_path = os.path.join(data_path, 'icon.png').replace("\\", "/")
        metadata_path = os.path.join(data_path, 'meta.json').replace("\\", "/")
        
        metadata = {}
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)
            metadata['name'] = data_name

        if not REMOTE:
            metadata['image'] = os.path.join(data_path, 'icon.png').replace("\\", "/")

        datas.append(
            metadata
        )

    # datas.sort(key=lambda x: sort_func(x['team'])) 

    # 生成 HTML
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>EditionView</title>
        <script src="https://cdn.tailwindcss.com"></script>
    <style>
    body {
        font-family: sans-serif;
        background-color: #bbaf98;
        background-size: 100%;                  /* 拉伸以覆盖整个区域 */
        background-repeat: repeat;            /* 不重复平铺 */
    }
    .statement {
        margin-right: 20px;
        margin-left: 20px;
        margin-top: 10px;
        margin-bottom: 10px;
        padding: 10px;
        text-align: left;
        background-color: #d9d0be;
        height: 150px;
        font-size: 14px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        z-index: 1001;
    }
    .content_body {
        background-color: #f4ece1;
        margin-right: 5vw;
        margin-left: 5vw;
        padding: 20px;
    }
    
    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    }
    .item {
        border-radius: 0px;
        padding: 0px;
        display: flex; /* 横向排列 */
        text-align: center;
    }
    .item img {
        width: 70px;
        height: 70px;
        object-fit: contain;
    }
    .item p {
        text-align: left;
        margin-right: 10px;
        margin-top: 10px;
        font-size: 12px;
        color: #333;
    }

    /* Collapsible Filter Styling */
    details > summary {
        list-style: none; /* Remove default marker */
        cursor: pointer;
        padding: 10px;
        background-color: #f9fafb; /* Light gray background for summary */
        border-radius: 8px;
        font-weight: 600;
        color: #1f2937; /* Dark gray text */
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    details > summary::-webkit-details-marker {
        display: none; /* Hide marker in Chrome/Safari */
    }
    details > summary::after { /* Custom arrow indicator */
        content: '▼'; /* Down arrow */
        font-size: 0.8em;
        transition: transform 0.2s ease-in-out;
    }
    details[open] > summary::after {
        transform: rotate(180deg); /* Rotate arrow when open */
    }
</style>
    """

    logo = 'https://clocktower.gstonegames.com/images/logo.png'
    if 'logo' in meta:
        logo = meta['logo']

    html += f"""
    </head>

    <body>
    <div class="content_body">

	<div style="display: flex; justify-content: center;" >
    """

    if 'state' in meta:
        # Add image
        html += f"""	
        <div style="width: 100vw; align-items: center;">
        <img style="width: 100%; height: 120px;" src="{logo}">
        <div style="text-align: left; font-size: 14px;">
	剧本作者：{AUTHOR}<br>
	支持人数： 5-9人
	</div>
        </div>
        """
        
        # Add state
        all_states = ''
        for stateent in meta['state']:
            all_states = all_states + '<b>'+ stateent['stateName'] +'</b> '
            all_states = all_states + stateent['stateDescription'] + '<br>\n'

        html += f"""<div class="statement" > {all_states} </div>"""
    
    else:
        # Only add image
        html += f"""	
        <div style="width: 40vw; align-items: center;">
        <img style="width: 100%; height: auto;" src="{logo}">
        </div>
        """

    # author info
    html += f"""
	</div>

    """

    # with open("htmls/skins_top.html", "r", encoding="utf-8") as f:
    #    html += f.read()
            
    with open("htmls/tag_line.html", "r", encoding="utf-8") as f:
        html += f.read()
        
    # Yan_ice:
    # Here display: none is used to get more space.

    html += """
    <details style="display: none;"
      class="mb-6 bg-white rounded-lg shadow overflow-hidden">
        <summary class="text-lg">
            <span>筛选与排序选项</span>
            </summary>
        <div class="p-4">
    """
    with open("htmls/util.html", "r", encoding="utf-8") as f:
        html += f.read()

    with open("htmls/choice_group.html", "r", encoding="utf-8") as f:
        html += f.read()

    with open("htmls/sort_method.html", "r", encoding="utf-8") as f:
        html += f.read()

    with open("htmls/category_method.html", "r", encoding="utf-8") as f:
        html += f.read()

    with open("htmls/tag_choose.html", "r", encoding="utf-8") as f:
        html += f.read()
        
    html += """ 
    </div>
    </details>

    <hr><div id="character_content"> 
    """

    # 添加每个图标+文字组合
    for item in datas:
        tag_seri = ''
        for a in item['tags']:
            tag_seri = tag_seri + a + '_'
        html += f"""
            <div class="item" data-name={item['name']} data-team={sort_func(item['team'])} data-tag={tag_seri} >
                <img src="{item['image']}" alt="{item['name']}"> 
                <p> <b>{item['name']}</b> <br> {item['ability']}</p>
            </div>
        """

    # 结束 HTML
    
    html += """
    </div>
    <script>

    var items_all;

    function init() {
        const grid = document.getElementById('character_content');
        items_all = Array.from(grid.getElementsByClassName('item'));
        console.log("初始化逻辑已执行。");
        update();
    }

    // 页面 DOM 加载完成后执行 init
    document.addEventListener("DOMContentLoaded", init);

    function update() {
        const content = document.getElementById('character_content');
        
        content.replaceChildren();
        var items = Array.from(items_all);

        items = items.filter(rule_type_filter);

        items = items.filter(rule_tag_filter);
        // 按 data-name 排序
        //item = items.sort(rule_sort);

        const [cate_items, colors] = rule_cate(items);
        Object.keys(cate_items).forEach((key) => {
            const list = cate_items[key];
            if (list.length > 0) {
                const container = document.createElement('div');
                container.className = 'grid';
                
                list.forEach((x)=>{
                    container.appendChild(x);
                });
                const head = create_splitline(key, colors[key]);
                content.appendChild(head);
                content.appendChild(container);
            }
            
        })
        
    }
    </script>
    """



    ############### temp night order ########

    with open("htmls/night_order.html", "r", encoding="utf-8") as f:
            html += f.read()

    firstnight = load_first_night_order()

    html += """
    <div class="left-fixed">
    """
    
    html += f""" <div class = "side-icon"><img src="../resources/night.jpg"></div> """
    html += f""" <div class = "side-icon"><img src="../resources/minion.jpg"></div> """
    html += f""" <div class = "side-icon"><img src="../resources/demon.jpg"></div> """

    for charac in firstnight:
        img = load_character_meta(charac)['image']
        html += f""" <div class = "side-icon"><img src="{img}"></div> """

    html += f""" <div class = "side-icon"><img src="../resources/day.jpg"></div> """

    html+="""
    </div>
    """

    firstnight = load_other_night_order()

    html += """
    <div class="right-fixed">
    """
    html += f""" <div class = "side-icon"><img src="../resources/night.jpg"></div> """
    for charac in firstnight:
        img = load_character_meta(charac)['image']
        html += f""" <div class = "side-icon"><img src="{img}"></div> """

    html += f""" <div class = "side-icon"><img src="../resources/day.jpg"></div> """

    html+="""
    </div>
    """

    ##########################################

    #with open("htmls/skins_bottom.html", "r", encoding="utf-8") as f:
    #        html += f.read()

    today = datetime.date.today()

    html += f""" 
    <p class="text-center">
        <br>每个夜晚* 表示从第二个夜晚开始生效。 <br>
    </p>
       
    <hr>
    <p class="text-center text-sm text-gray-500">
        {EDITION_NAME}_{VERSION} | generated by EditionPdf Generator | {today}
    </p>

    </div>
    </body>
    """
    os.makedirs(f"output", exist_ok=True)

    # 保存为 HTML 文件
    with open(f"output/{file_name}.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"已生成 output/{file_name}.html 文件，可以用浏览器打开查看效果。")
