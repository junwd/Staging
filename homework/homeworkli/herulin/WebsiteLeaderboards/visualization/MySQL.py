import logging
import pymysql
def selectdata(sqlstr):
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           password='root', db='gen',
                           charset="utf8")
    cursor = conn.cursor()  # 建立一个游标对象
    try:
        cursor.execute(sqlstr)  #使用游标执行SQL语句
        conn.commit() #提交数据
        #  print(cursor.rowcount) 输出查询记录数
        return cursor.fetchall()  #  获取全部记录
        #  return SqlDomainName
        cursor.close() #关闭游标对象
        conn.close()#关闭连接
    except Exception as e:
        # 有异常，回滚事务
        logging.exception(e)
        conn.rollback() #撤销数据
