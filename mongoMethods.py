# coding: utf-8
'''
Some methods about pymongo
'''
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client.test_database # get the database
#collection = db.test_collection # get the collection
posts = db.posts
post = {'author': 'zjy',
        'text': 'my first post',
        'tags': ['mongodb', 'python', 'pymongo'],
        'date': datetime.datetime.utcnow()}
post_id = posts.insert_one(post).inserted_id
print post_id
print db.collection_names(include_system_collections=False) # print all collections in db
print posts.find_one()
print posts.find_one({'author': 'zjy'})
print posts.find_one({'author': 'zhujy'})
print posts.find_one({'_id': post_id})
print posts.count()

for result in posts.find({'author': 'zjy'}):
    print result