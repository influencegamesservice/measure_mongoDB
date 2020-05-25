import unittest
from pymongo import MongoClient, ASCENDING
from datetime import datetime
import sys
import json
import random
import time
import logging
import numpy as np

class Testmongodb:

    def __init__(self):
        self.DB_of_Test = MongoClient()['Test']
        self.COLLECTION_of_Test = self.DB_of_Test.Test

        self.logger = self.__get_logger()
    
    def __get_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        self.__set_logger_FileHandler(logger, "/home/data/log/test_mongoDB/root.log")

        return logger
    
    def __set_logger_FileHandler(self, logger, log_file_path):
        get_handler = logging.FileHandler(log_file_path)
        logger.addHandler(get_handler)
    
    def measure_insert_one(self, list_doc):
        self.COLLECTION_of_Test.delete_many({})

        insert_one_sta = time.perf_counter()
        for doc in list_doc:
            self.COLLECTION_of_Test.insert_one(doc)
        insert_one_end = time.perf_counter()

        insert_one_time = insert_one_end - insert_one_sta

        log = "insert_one_time = {0}[sec]".format(insert_one_time)
        self.logger.info(log)
    
    def measure_insert_one_with_index(self, list_doc, list_index_model):
        self.COLLECTION_of_Test.delete_many({})
        self.COLLECTION_of_Test.create_indexes(list_index_model)

        insert_one_with_index_sta = time.perf_counter()
        for doc in list_doc:
            self.COLLECTION_of_Test.insert_one(doc)
        insert_one_with_index_end = time.perf_counter()

        insert_one_with_index_time = insert_one_with_index_end - insert_one_with_index_sta

        log = "insert_one_with_index_time = {0}[sec]".format(insert_one_with_index_time)
        self.logger.info(log)

        self.COLLECTION_of_Test.drop_indexes()

    def measure_insert_many(self, list_doc):
        self.COLLECTION_of_Test.delete_many({})

        insert_many_sta = time.perf_counter()
        self.COLLECTION_of_Test.insert_many(list_doc)
        insert_many_end = time.perf_counter()

        insert_many_time = insert_many_end - insert_many_sta

        log = "insert_many_time = {0}[sec]".format(insert_many_time)
        self.logger.info(log)
    
    def measure_insert_many_with_index(self, list_doc, list_index_model):
        self.COLLECTION_of_Test.delete_many({})
        self.COLLECTION_of_Test.create_indexes(list_index_model)

        insert_many_with_index_sta = time.perf_counter()
        self.COLLECTION_of_Test.insert_many(list_doc)
        insert_many_with_index_end = time.perf_counter()

        insert_many_with_index_time = insert_many_with_index_end - insert_many_with_index_sta

        log = "insert_many_with_index = {0}[sec]".format(insert_many_with_index_time)
        self.logger.info(log)

        self.COLLECTION_of_Test.drop_indexes()