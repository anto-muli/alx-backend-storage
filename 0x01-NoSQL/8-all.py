#!/usr/bin/env python3
"""" MongoDB operations with Python using pymongo """

def list_all(mongo_collection):
    """ List all docs in a oython file"""
    documents = mongo_collection.find()
    
    if documents.count() == 0:
        return[]
    
    return documents