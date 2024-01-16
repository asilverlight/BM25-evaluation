import json
import os
import argparse
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='summary bm25 results')
    parser.add_argument('--input-folder', required=True, help='initial runs path')
    parser.add_argument('--output-file', required=True, help='merged runs path')
    
    args = parser.parse_args()
    tsv_files = [f for f in os.listdir(args.input_folder) if f.endswith('.tsv')]

    # with open(args.output_file, 'w') as fw:

    #     # 遍历每个 .tsv 文件并将内容写入到大文件中
    #     for tsv_file in tsv_files:
    #         file_path = os.path.join(args.input_folder, tsv_file)
    #         with open(file_path, 'r') as fr:
    #             # 将每行数据写入到大文件中
    #             for line in fr:
    #                 fw.write(line)
    tsv_file = open(args.output_file, 'w', encoding='utf-8', newline='\n')
    tsv_writer = csv.writer(tsv_file, delimiter='\t')
    for tfile in tsv_files:
        file_path = os.path.join(args.input_folder, tfile)
        with open(file_path, "r", encoding="utf-8") as fr:
            for line in fr:
                qid, docid, num = map(int, line.strip().split())
                tsv_writer.writerow([qid, docid, num])