#%%
import pymongo

class MongoDb:
    def __init__(self, url):
        client = pymongo.MongoClient(url)
        db = client['Lotto']
        self.scratch_cards = db['scratch_cards']
