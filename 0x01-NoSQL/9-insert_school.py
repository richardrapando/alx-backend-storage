#!/usr/bin/env python3
'''MongoDB Operations with Python
'''

def insert_school(mongo_collection, **kwargs):
    '''New document inserted in collection.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
