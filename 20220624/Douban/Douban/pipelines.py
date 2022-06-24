# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs  # 导入包
import json  # 导入包

# from itemadapter import ItemAdapter


class DoubanPipeline:
    def process_item(self, item, spider):
        print(item["name"])  # 打印出名称，查看名称是否正确 item用于接收items


class DoubanPipeline_json:  # 设置项目管道
    def __init__(self):
        self.file = codecs.open('Douban.json', 'w', encoding="utf-8")  # json名，设置为utf-8编码

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 保存item数据并换行
        self.file.write(lines)
        return item  # 接收item数据

    def spider_closed(self, spider):
        self.file.close()



from openpyxl import Workbook

class DoubanPipeline_excel(object):
    def __init__(self):
        self.wb = Workbook() # 类实例化
        self.ws = self.wb.active # 激活工作表
        self.ws.append(['电影名称']) # 添加表头
    def process_item(self, item, spider):
        data = [item["name"]]
        self.ws.append(data) # 将数据以行的形式添加到工作表中
        self.wb.save('Earth.xlsx') # 保存
        return item

