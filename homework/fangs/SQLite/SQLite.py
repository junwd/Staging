import sqlite3  # 数据库

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT cname,COUNT(*) AS COUNT FROM movie250 GROUP BY cname HAVING COUNT>1'
# sql = 'select introduction from movie250'
data = cur.execute(sql)
for i in data:
    x=i[0]
    y=i[1]
    print(x,y)
cur.close()
con.close()
