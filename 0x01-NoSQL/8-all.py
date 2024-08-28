#!/usr/bin/env python3
"""
This function lists all document in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    list all documents
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
