# 智能剧本打印器
一款可以直接将json文件生成为打印剧本的生成器！
👇👇👇一个简单的例子如下👇👇👇
![example.png](example.png)
创作该剧本只使用了10秒钟噢

## 项目结构
`config/` 存有剧本的基本设置。

`data/` 从json读取的所有角色数据（缓存）。

`htmls/` 存有所有剧本html的辅助功能，会被python脚本整合成一个大html。

`output/` 将保存生成的剧本。

`pysrc/` 存有所有主要python代码。

`util/` 存有一些乱七八糟但有用的东西，和项目本身关系不大）

`main.py` 生成器主程序，通过main.py执行各种功能。


## 快速上手

请确保你安装了python3.8以上，并建议在Ubuntu20.04环境运行。

1. Python 环境配置

```
pip install requests beautifulsoup4
```

2. 加载一个json

```
python3 main.py fetch <JSON文件路径>
```

3. 生成html剧本

```
python3 main.py gen
```

4. 用浏览器打开output/XX.html，打印剧本，完工

## 待办清单

1. 美化

## 参与维护/联系我们

(不是鱼子酱)邮箱：yan2364728692@gmail.com

欢迎给项目提交PR或共同成为维护者
