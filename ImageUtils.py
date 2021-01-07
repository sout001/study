import time
import requests
from bs4 import BeautifulSoup
import os

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                        '/86.0.4240.75 Safari/537.36'}


def GetImageUtils(url):
    try:
        req = requests.get(url, timeout=30, headers=header)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        return req.text
    except:
        return ''


if __name__ == '__main__':
    # folder_name = 'test'
    # if not os.path.exists(folder_name):
    #     # 创建文件夹
    #     os.mkdir(folder_name)
    # else:
    #     print("该文件夹已存在")
    # # 返回folder文件夹在系统中的绝对路径
    # print(os.path.abspath(folder_name))
    # # 获取当前系统登录用户
    # print(os.getlogin())
    # print(os.getenv)
    # print(os.path.join(os.path.expanduser('~'), "Desktop"))
    # xb = os.path.join(os.path.expanduser('~'), 'Desktop')
    # if os.path.isdir(folder_name):
    #     with open(xb + '/test2.txt', mode='w', encoding='utf-8') as f:
    #         f.write("当前登录用户是：" + os.getlogin())
    #         f.close()
    #         print("看你的桌面")
    # else:
    #     print("它不是一个目录")
    folder_path = 'D:\Downloads\2.png'
    if os.path.isfile(folder_path):
        with open(folder_path, 'wb+') as f:
            t = f.read()
            f.close()
            print(t)
