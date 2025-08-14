#!/usr/bin/env python3
"""Python function that changes all topics of a school document"""


from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    mongo_collection.update_one(
        {"name": name}, {"$set": {"topics": topics}}
    )
