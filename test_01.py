# _*_ codding:utf-8 _*_
# Created by GMCY
# https://blog.csdn.net/weixin_46554689
# 2020/4/26

import jieba


def ai_StrSplit(String):
    """
    Decompose the string into a list           # 将字符串分解为一个列表
    :param String: The string to be decomposed # 要分解的字符串
    :return: String_lt                         # 分解后的字符串列表
    """
    String_lt = jieba.lcut(String, cut_all=True)  # 要引入jieba库
    String1 = jieba.lcut(String, cut_all=True)
    String2 = jieba.lcut(String, cut_all=True)
    String3 = jieba.lcut(String, cut_all=True)
    String3.append('')
    for Str1 in String1:
        String2.remove(Str1)
        for Str2 in String2:
            try:
                String3.remove(Str1)
            except:
                pass
            try:
                String3.remove(Str2)
            except:
                pass
            for Str3 in String3:
                String_lt.append(Str1 + Str2 + Str3)
    return String_lt


def ai_MatchSiple(path, String):
    """
    Matches the dictionary to a single string  # 将字典匹配到单个字符串
    :param path: The dictionary to match       # 匹配的字典
    :param String: The string to match         # 要匹配的字符串
    :return: lt_ms                             # 匹配结果与判断(1有/0无)的列表
    """
    errow_matchsplit = 0
    back = None
    with open(path, 'r', encoding='utf-8') as f:  # 注意编码
        while errow_matchsplit == 0:
            f1 = f.readline().split('\n')[0]
            f2 = f.readline().split('\n')[0]
            f3 = f.readline()
            if String == f1:
                back = f2
                errow_matchsplit = 1
                break
            if f1 == '' or f2 == '':
                break
    lt_ms = [back, errow_matchsplit]
    return lt_ms


def ai_MatchHeight(path, String_lt):
    """
    Matches the dictionary with a list of strings # 用字符串列表匹配字典
    :param path: The dictionary to match          # 匹配的字典
    :param String_lt: List of strings to match    # 要匹配的字符串列表
    :return: lt_mh                                # 匹配结果与判断(1有/0无)的列表
    """
    errow_matchheight = 0
    back = None
    with open(path, 'r', encoding='utf-8') as f:  # 注意编码
        while errow_matchheight == 0:
            f1 = f.readline().split('\n')[0]
            f2 = f.readline().split('\n')[0]
            f3 = f.readline()
            for String in String_lt:
                if String == f1:
                    back = f2
                    errow_matchheight = 1
                    break
            if f1 == '' or f2 == '':
                break
    lt_mh = [back, errow_matchheight]
    return lt_mh


def ai_study(path, study_start, study_end):
    """
    Open the dictionary and write the match statement and the match result # 打开字典并编写匹配语句和匹配结果
    :param path: The dictionary to open                                    # 要查的字典
    :param study_start: Dictionary matching statements                     # 词典匹配语句
    :param study_end: The dictionary returns the result                    # 字典返回结果
    :return: None                                                          # 无返回
    """
    with open(path, 'a', encoding='utf-8') as f:  # 注意编码
        f.write(study_start + '\n')
        f.write(study_end + '\n')
        f.write('\n')


if __name__ == '__main__':
    path = r'ai词库.txt'  # 要匹配的词典
    print('=' * 20 + '程序开始' + '=' * 20)
    print('小艾: 主人是否要加载学习模块')
    errow_study = input('主人(y/n):')
    print('小艾: 主人请吩咐')
    String = input('主人: ')
    while String != 'exit':
        a1 = ai_MatchSiple(path=path, String=String)
        show = a1[0]
        errow_matchsimple = a1[1]
        if errow_matchsimple == 0:
            String_lt = ai_StrSplit(String=String)
            a2 = ai_MatchHeight(path=path, String_lt=String_lt)
            show = a2[0]
            errow_matchhight = a2[1]
            if errow_matchhight == 0 and (errow_study == 'y' or errow_study == 'yes'):
                print('小艾: 请主人输入要学习语句(n退出学习)')
                study_start = input('主人: ')
                if study_start != 'n' and study_start != 'no':
                    print('小艾: 请主人输入回答语句(n退出学习)')
                    study_end = input('主人: ')
                    if study_end != 'n' and study_end != 'no':
                        print('小艾: 加载中…')
                        ai_study(path=path, study_start=study_start, study_end=study_end)
                        print('小艾: 加载完成')
            else:
                print('小艾:', show)
        else:
            print('小艾:', show)
        String = input('主人: ')
    print('=' * 20 + '程序结束' + '=' * 20)
