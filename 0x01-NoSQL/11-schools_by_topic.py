#!/usr/bin/env python3
""" MongoDB Ops using pymongo"""


def schools_by_top(mongo_collection, topic):
    """ return a list of schools with specific topics"""
    documents = mongo_collection.find({"topics": topic})
    return list(documents)