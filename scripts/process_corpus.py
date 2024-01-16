import json
import os
import argparse
import tqdm

def process(args):
    print('Processing......')
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    file_index = 0
    with open(args.collection_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            docid, title, text = data["docid"], data["title"], data["text"]
            if i % args.max_docs_per_file == 0:
                if i > 0:
                    output_jsonl_file.close()
                output_path = os.path.join(args.output_folder, 'docs{:02d}.json'.format(file_index))
                output_jsonl_file = open(output_path, 'w', encoding='utf-8', newline='\n')
                file_index += 1
            output_dict = {'id': docid, 'contents': title + " " + text}
            output_jsonl_file.write(json.dumps(output_dict) + '\n')
            
            if i % 100000 == 0:
                print(f'Converted {i:,} docs, writing into file {file_index}')
    #获取目标corpus名称地址
    output_jsonl_file.close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='process corpus for bm25')
    parser.add_argument('--collection-path', required=True, help='Path to MS MARCO collection.')
    parser.add_argument('--output-folder', required=True, help='Output folder.')
    parser.add_argument('--max-docs-per-file', default=1000000, type=int,
                        help='Maximum number of documents in each jsonl file.')

    args = parser.parse_args()



    process(args)
    print('Done!')