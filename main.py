from scrapy import cmdline
import os
import sys

# 将系统当前目录设置为项目根目录
# os.path.abspath(__file__)为当前文件所在绝对路径
# os.path.dirname为文件所在目录
# 由于启动文件在根目录，此文件可没有
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 执行命令，相当于在控制台cmd输入改名了
cmdline.execute(["scrapy", "crawl", "administrative-division"])
