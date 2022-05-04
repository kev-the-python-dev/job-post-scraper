import pymongo
import logging

'''This pipeline is made specifically to import the data we extract from our spider into a MongoDB database called job_posts. Unfortunately a database must already be created (as well as a collection) for this to work.'''

class MongoPipeline(object):
    '''Required. If you change this, you MUST update your MongoDB database to match the collection name below, e.g. if collection is changed to "mega_jobs" you must have a collection already created called "mega_jobs".'''
    collection_name = 'jobs'
    
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    # The Below class definitions are standard of PyMongo (view documentation).
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                # Saves us time and anytime we need to update the Server/DB we can do via settings instead of having to change both here and settings.
                mongo_uri=crawler.settings.get('MONGODB_SERVER'),
                mongo_db=crawler.settings.get('MONGODB_DB')
                )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # Playing with insert_one() and insert() to see which performs faster and more accurately. 
        self.db[self.collection_name].insert_one(dict(item))
        logging.debug("Job post added to MongoDB")
        return item
