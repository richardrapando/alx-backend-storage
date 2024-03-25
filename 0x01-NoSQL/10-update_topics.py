#!/usr/bin/env python3
'''MongoDB Operations with Python
'''


def update_topics(mongo_collection, name, topics):
    '''All topics of a school document changed based on name
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
