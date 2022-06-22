import sqlite3  # 数据库

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT main.movie250.cname,main.movie250.score,main.movie250.year_release FROM main.movie250 ORDER BY main.movie250.score ASC LIMIT 20'
data = cur.execute(sql)
for i in data:
    # x=i[1]
    y=i[1]
    # z=i[2]
    print(y)
cur.close()
con.close()
