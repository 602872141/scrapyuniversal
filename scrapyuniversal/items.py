# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose, MapCompose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())



def handle_source(value):
    type(value)
    return value.strip()
def tiem(value):
    type(value)
    return value
def handle_text(value):
    addr_list = value.split("\n")
    addr_list = [item.strip() for item in addr_list ]
    type(addr_list)
    return "".join(addr_list)




class NewsItem(Item):
    title = Field()
    url = Field()
    url_id=Field()
    text = Field(

        input_processor=MapCompose(handle_text),
    )
    datetime = Field(
        input_processor=MapCompose(tiem),
    )
    source = Field(
    input_processor=MapCompose(handle_source),
    )
    website = Field()

    # def get_insert_sql(self):
    #         insert_sql = """
    #             insert into lagou_job(title, url, url_object_id, salary, job_city, work_years, degree_need,
    #             job_type, publish_time, job_advantage, job_desc, job_addr, company_name, company_url,
    #             tags, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    #             ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_desc=VALUES(job_desc)
    #         """
    #         params = (
    #             self["title"], self["url"], self["url_object_id"], self["salary"], self["job_city"],
    #             self["work_years"], self["degree_need"], self["job_type"],
    #             self["publish_time"], self["job_advantage"], self["job_desc"],
    #             self["job_addr"], self["company_name"], self["company_url"],
    #             self["job_addr"], self["crawl_time"].strftime(SQL_DATETIME_FORMAT),
    #         )
    #
    #         return insert_sql, params