import os
import json
import logging
import inspect
import numpy as np
from tqdm import tqdm
import csv

file_path = "/share/peitian/Data/Datasets/llm-embedder/qa/msmarco/train.json"

#打开.tsv文件并统计数据行数
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        if data["query_id"] == int('315'):
            print("yes")
            break

# 输出文件的数据行数
