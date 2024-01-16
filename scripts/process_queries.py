import json
import os
import argparse
import csv

def process(args):
    print('Processing......')
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    file_index = 0
    with open(args.collection_path, 'r', encoding='utf-8') as f:
        tsv_writer = None
        records_written = 0
        
        for line in f:
            data = json.loads(line)
            query_id = data["query_id"]
            query = data["query"]
            
            if tsv_writer is None or records_written % args.max_queries_per_file == 0:
                if tsv_writer is not None:
                    tsv_file.close()
                tsv_file_path = os.path.join(args.output_folder, f'queries_{file_index}.tsv')
                tsv_file = open(tsv_file_path, 'w', encoding='utf-8', newline='\n')
                tsv_writer = csv.writer(tsv_file, delimiter='\t')
                file_index += 1
            
            tsv_writer.writerow([query_id, query])
            records_written += 1
            
    if tsv_writer is not None:
        tsv_file.close()
      

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='process queries for bm25')
    parser.add_argument('--collection-path', required=True, help='Path to MS MARCO collection.')
    parser.add_argument('--output-folder', required=True, help='Output folder.')
    parser.add_argument('--max-queries-per-file', default=10000, type=int,
                        help='Maximum number of queries in each jsonl file.')

    args = parser.parse_args()



    process(args)
    print('Done!')