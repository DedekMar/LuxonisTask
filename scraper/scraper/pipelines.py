# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter

from sqlalchemy.orm import sessionmaker

from scraper.models import Estates
from scraper.base import db_connect, create_estates_table


class ScraperPipeline:

    def __init__(self):
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)
        create_estates_table(engine)


    def process_item(self, item, spider):
        session = self.Session()

        estate = Estates(**item)

        try:
            session.add(estate)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
