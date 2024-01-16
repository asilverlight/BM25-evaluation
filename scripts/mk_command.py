import json
import os
import argparse

if __name__ == '__main__':
    files_and_folders = os.listdir('/share/yutao/yifei/bm25_data/queries')
    files = [item for item in files_and_folders if os.path.isfile(os.path.join('/share/yutao/yifei/bm25_data/queries', item))]
    num = len(files)
    with open('commands.txt', 'w') as fw:
        for i in range(num):
            fw.write(f'/share/peitian/Apps/anserini/target/appassembler/bin/SearchCollection -index /share/yutao/yifei/bm25_data/index_msmarco -topics /share/yutao/yifei/bm25_data/queries/queries_{i}.tsv -topicreader TsvInt -output /share/yutao/yifei/bm25_data/output_runs/run.msmarco-passage.{i}.tsv -format msmarco -parallelism 4 -bm25 -bm25.k1 0.82 -bm25.b 0.68 -hits 1000\n')
    text = "/share/yutao/yifei/bm25_data/output_runs/run.msmarco.tsv"