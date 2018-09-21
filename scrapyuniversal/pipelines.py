# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql


class ScrapyuniversalPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    conn = pymysql.connect(host='localhost', user='root', password='root', charset="utf8", use_unicode=True,
                              db="sys")
    cursor = conn.cursor()
    def process_item(self, item, spider):
        data={
            'title':item["title"],
            'url':item["url"],
            'url_id':item["url_id"],
            'text':item["text"],
            'datetime': item["datetime"],
            'source': item["source"],
            'website':item["website"]
        }
        table="zhong"
        keys = ",".join(data.keys())
        values=",".join(['%s']*len(data))
        sql = ' insert into {table}({key})VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table,key=keys,values=values)
        update=','.join("{key} = %s" .format(key=key)for key in data.keys())
        insert_sql=sql+update
        self.cursor.execute(insert_sql,tuple(data.values())*2)
        self.conn.commit()
        return item
        # insert_sql = """insert into zhong(title, url,url_id, text, datetime,source,website)VALUES (%s, %s, %s, %s, %s,%s, %s)"""
        # self.cursor.execute(insert_sql, (item["title"], item["url"], item["url_id"], item["text"], item["datetime"], item["source"], item["website"]))
        # self.conn.commit()

class mongdb_pipelines(object):

    def process_item(self, item, spider):
        # data = {
        #     'title': item["title"],
        #     'url': item["url"],
        #     'url_id': item["url_id"],
        #     'text': item["text"],
        #     'datetime': item["datetime"],
        #     'source': item["source"],
        #     'website': item["website"]
        # }
        client = pymongo.MongoClient(host="localhost")
        db = client['new']
        db['new'].insert_one(dict(item))
        return item