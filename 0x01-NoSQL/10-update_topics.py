#!/usr/bin/env python3
""" MongoDB op using pymongo"""

def update_topics(mongo_collection, name, topics):
    """ Changes topics of a school doc used on the name"""
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    
    mongo_collection.update_many(query, new_values)