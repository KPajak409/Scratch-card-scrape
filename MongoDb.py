#%%
import pymongo

class MongoDb:
    def __init__(self, url):
        client = pymongo.MongoClient(url)
        db = client['Lotto']
        self.scratch_cards = db['scratch_cards']

    def insert_one(self, scratch_card):
        x = self.scratch_cards.insert_one(scratch_card)
        return x.inserted_id

    def find_one(self, filter):
        res = self.scratch_cards.find_one(filter)
