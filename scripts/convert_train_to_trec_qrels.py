#
# Pyserini: Python interface to the Anserini IR toolkit built on Lucene
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MS MARCO qrels to TREC qrels.')
    parser.add_argument('--input', required=True, default='', help='Input MS MARCO qrels file.')
    parser.add_argument('--output', required=True, default='', help='Output TREC qrels file.')

    args = parser.parse_args()

    # with open(args.output, 'w') as fout:
    #     for line in open(args.input):
    #         fout.write(line.replace('\t', ' '))
    with open(args.output, 'w', encoding="utf-8") as fw:
        with open(args.input, 'r', encoding="utf-8") as fr:
            for line in fr:
                data = json.loads(line)
                query_id = data["query_id"]
                pos_index = data["pos_index"]
                for pos_idx in pos_index:
                    fw.write(f"{query_id}'\t'0'\t'{pos_idx}'\t'1\n")

    print('Done!')
