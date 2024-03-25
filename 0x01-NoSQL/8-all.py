#!/usr/bin/env python3
'''MongoDB Operations with Python 
'''
def list_all(mongo_collection):
    '''All documents in a collection listed
    '''
    return [doc for doc in mongo_collection.find()]
