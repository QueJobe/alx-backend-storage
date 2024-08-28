#!/usr/bin/env python3
"""
search collection by topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Function to find topic
    """
    return mongo_collection.find({"topics": topic})
