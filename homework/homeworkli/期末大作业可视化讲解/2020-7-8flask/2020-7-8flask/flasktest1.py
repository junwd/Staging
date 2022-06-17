import json
from flask import Flask, render_template, url_for
from linkdatabase import selectdata

app = Flask(__name__)


@app.route('/getdata', methods=['GET', 'POST'])
def get_data():
    year = []
    count = []
    jsonData = {}  # 创建json数据

    sqlstr1 = "SELECT DATE_FORMAT(time, '% %Y' )as years ,\
             COUNT( * ) as counts FROM qnzynews \
             GROUP BY DATE_FORMAT( time, '% %Y' ) \
             ORDER BY years DESC"
    rows1 = selectdata(sqlstr1)
    print(rows1)

    for data in rows1:
        year.append(data[0])
        count.append(data[1])
    jsonData['year'] = year
    jsonData['count'] = count
    j = json.dumps(jsonData)
    return (j)


@app.route('/')
def my_tem():
    # 在浏览器上渲染my_templaces.html模板
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='192.168.11.201', port=9488, debug=True)
