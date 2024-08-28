#!/usr/bin/env python3
"""
function to change school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update collection
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
