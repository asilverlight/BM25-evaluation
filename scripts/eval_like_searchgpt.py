import os
import datasets
import numpy as np
from typing import List
from dataclasses import dataclass, field, asdict
from torch.utils.data import DataLoader
from collections import defaultdict
from accelerate import Accelerator
from transformers import HfArgumentParser
from transformers.utils import logging

from src import ModelArgs, Metric, DatasetProcessFn, DefaultDataCollator, FileLogger, get_model_and_tokenizer, makedirs

logger = logging.get_logger(__name__)

@dataclass
class Args(ModelArgs):
    eval_data: str = field(
        default='/share/peitian/Data/Datasets/llm-embedder/qa/msmarco/train.json',
        metadata={'help': 'The evaluation json data path.'}
    )
    bm25_results: str = field(
        default='/share/yutao/yifei/bm25_data/output_runs/run.msmarco.tsv',
        metadata={'help': 'The evaluation json data path.'}
    )
    output_dir: str = field(
        default="/share/yutao/yifei/bm25_data/results",
        metadata={'help': 'Output directory for results and logs.'}
    )
    metrics: List[str] = field(
        default_factory=lambda: ["mrr", "recall", "ndcg"],
        metadata={'help': 'List of metrics. {rouge, acc}'}
    )
    cutoffs: List[int] = field(
        default_factory=lambda: [1, 5, 10],
        metadata={'help': 'Cutoffs to evaluate retrieval metrics.'}
    )

def main():
    parser = HfArgumentParser([Args])
    args: Args = parser.parse_args_into_dataclasses()[0]
  
    from src import RerankResult
    import csv
    from tqdm import tqdm
    results = {}
    
    total1 = 0
    with open(args.bm25_results, 'r', encoding='utf-8') as fr:
        for line in fr:
            total1 += 1
    
    with open(args.bm25_results, 'r', encoding='utf-8') as fr:
        reader = csv.reader(fr, delimiter=' ')
        for row in tqdm(reader, total=total1, desc="Reading bm25 results"):
            qid, docid = row[0], row[1]
            results.setdefault(qid, [])
            results[qid].append(RerankResult(docid, 0))
    
    metrics = Metric.get_metric_fn(metric_names=args.metrics, eval_data=args.eval_data, cutoffs=args.cutoffs)(results=results)
    file_logger = FileLogger(makedirs(os.path.join(args.output_dir, "metrics.log")))
    file_logger.log(metrics, Args=asdict(args))

if __name__ == "__main__":
    main()