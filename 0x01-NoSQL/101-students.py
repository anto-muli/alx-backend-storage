#!/usr/bin/env python3
""" MongoDB Ops with Python using pymongo """


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """ Returns students sorted by average score """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student