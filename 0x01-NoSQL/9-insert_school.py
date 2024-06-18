#!/usr/bin/env python3
""" MongoDB operations with pymongo"""

def insert_school(mongo_collection, **kwargs):
    """ Insert a new doc using keywords"""
    return mongo_collection.insert(kwargs)