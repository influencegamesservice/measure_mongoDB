import numpy as np
import sys
import setting
from pymongo import IndexModel, ASCENDING

def rand_ints_nodup(from_n, to_n, get_count):
    return np.random.permutation(range(from_n, to_n))[:get_count]

arrand = [rand_ints_nodup(0, 10**7, setting.CREATE_DOCUMENT_COUNT) for _ in range(setting.CREATE_INDEX_COUNT)]

size_1k = [None] * 120

list_doc = []

for doc_count in range(setting.CREATE_DOCUMENT_COUNT):
    doc = {}

    doc["dummy_1k"] = size_1k

    for index_count in range(setting.CREATE_INDEX_COUNT):
        doc["dummy_number_{0}".format(index_count)] = int(arrand[index_count][doc_count])
    
    list_doc.append(doc)

print("list_doc 作成完了")

list_index_model = [IndexModel([("dummy_number_{0}".format(i), ASCENDING)]) for i in range(setting.CREATE_INDEX_COUNT)]