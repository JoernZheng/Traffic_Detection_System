import pymysql
import time
from main_module.tools import illegal_action_list


def main():
    connect = pymysql.connect('129.211.174.111', port=3306, user='Intelligence', passwd='L4FZNyBJAWWnRAjR', db='Intelligence')
    cursor = connect.cursor()
    sql1 = 'insert into illegalbook (location, action, license, picture_path) values (%s,%s, %s, %s)'  # 更新数据库
    sql2 = 'insert into carcountbook (location, count) values (%s, %s)'  # 更新数据库
    cursor.executemany(sql1, [('1234', '1234', '1234', '1234')])  #
    cursor.executemany(sql2, [('1234', 5)])  #

def insertIllegal(Objects, location, path):
    book = []
    for license in Objects:
        breakRule = ''
        for break_rule in Objects[license]:
            breakRule = breakRule + break_rule + ' '
        book.append((location, breakRule, license, path))
    connect = pymysql.connect('129.211.174.111', port=3306, user='Intelligence', passwd='L4FZNyBJAWWnRAjR', db='Intelligence')
    cursor = connect.cursor()
    sql = 'insert into illegalbook (location, action, license, picture_path) values (%s,%s, %s, %s)'  # 更新数据库
    cursor.executemany(sql, book)
    print('----------违规信息上传成功-------------')
    cursor.close()


def insertCount(location, count):
    connect = pymysql.connect('129.211.174.111', port=3306, user='Intelligence', passwd='L4FZNyBJAWWnRAjR', db='Intelligence')
    cursor = connect.cursor()
    sql = 'insert into carcountbook (location, count) values (%s, %s)'  # 更新数据库
    cursor.executemany(sql, [(location, count)])
    cursor.close()


if __name__ == '__main__':
    record = {'123': {'1', '2', '3'}, '234': {'2', '3', '4'}}
    insertIllegal(record, '中国矿业大学', '/')