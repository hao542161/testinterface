"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:connectmysql.py
@Software:PyCharm
@Desc:连接mysql数据库
"""
import pymysql
from commont import readconfig as rc


# 连接数据库
def connect():
    db = pymysql.connect(host=rc.get_db('host'),
                         user=rc.get_db('user'),
                         password=rc.get_db('password'),
                         port=int(rc.get_db('port')),
                         database=rc.get_db('database'))
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    db.commit()
    print('已连接mysql数据库：' + data[0])
    return db


# 插入语句
def insert(sql, args):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


# 插入多条
def insert_many(sql, args):
    conn = connect()
    cur = conn.cursor()
    result = cur.executemany(query=sql, args=args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


# 更新操作
def update(sql, args):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


# 删除数据
def delete(sql, args):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


# 查询所有数据
def queryall(sql, args):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results


# 查询首条数据
def queryone(sql, args):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    results = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return results


if __name__ == '__main__':
    # 插入一条
    # sql = 'INSERT INTO user VALUES(%s,%s,%s,%s,%s,%s)'
    # insert(sql, (None, 'test', '123456', '10', '15757191674', 'hangzhou'))
    # # 插入多条
    # sql = 'INSERT INTO user VALUES(%s,%s,%s,%s,%s,%s)'
    # args = [(None, 'test', '123456', '10', '15757191674', 'hangzhou'),
    #         (None, 'test', '123456', '10', '15757191674', 'hangzhou'),
    #         (None, 'test', '123456', '10', '15757191674', 'hangzhou')]
    # insert_many(sql, args)
    # # 更新
    # sql = 'UPDATE user SET username=%s WHERE userid = %s;'
    # args = ('haha', '9')
    # update(sql, args)
    # 删除
    # sql = 'DELETE FROM user WHERE userid = %s;'
    # args = ('10',)  # 单个元素的tuple写法
    # delete(sql, args)
    # 查询全部数据
    # sql = 'SELECT  * FROM user'
    # result = queryall(sql,None)
    # print(result)
    # 查询首条数据
    sql = 'SELECT  * FROM user WHERE username = %s'
    args = ('test',)
    result = queryone(sql, args)
    print(result)
