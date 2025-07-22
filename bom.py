# 将含有 UTF-8 BOM 的 JSON 文件转换为纯 UTF-8 格式

input_path = '假面.json'
output_path = '假面圆舞曲.json'

with open(input_path, 'r', encoding='utf-8-sig') as infile:
    content = infile.read()

with open(output_path, 'w', encoding='utf-8') as outfile:
    outfile.write(content)

print("转换完成，文件已保存为 UTF-8 无 BOM 格式。")

