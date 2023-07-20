#%%
import pymongo

my_client = pymongo.MongoClient('mongodb://localhost:27017')

my_db = my_client['Lotto']

scratch_cards = my_db['scratch_cards']

def insert_one(scratch_card):
    x = scratch_cards.insert_one(scratch_card)
    return x.inserted_id
#&&
# %%
print(scratch_cards.find_one())