import json
import torch
import pathlib

from copy import deepcopy
from torch.utils.data import Dataset

def build_qa_samples(tokenizer, data_dict, max_position_embeddings, split_name, logger):
    """
    构建 QA 模型训练所需的样本

    :param tokenizer:
        分词器，用于处理 question 和 context

    :param data_dict: dict
        JSONL 文件中的一条数据记录，
        应包含 QA 任务所需的相关字段

    :param max_position_embeddings: int
        模型允许的最大输入序列长度

    :param split_name: str
        当前数据集的名称，可选：
        "train"、"valid"、"test"、"visualize"

    :param logger:
        日志记录器

    :return: samples: list
        当前数据记录生成的 QA 样本列表

    📋📋📋📋
    请实现一个 QA 样本构建方法：
    根据输入的数据记录构建模型所需的 QA 样本，
    并将生成的样本组织成列表返回。

    请在下方完成你的实现
    """
    raise NotImplementedError("build_qa_samples 未实现")


class QADataset(Dataset):

    def __init__(
        self,
        data_file_path,
        tokenizer,
        split_name,
        progress_interval,
        read_interval,
        logger=None,
        max_position_embeddings=None,
    ):
        """
        QA 数据集构造函数

        :param data_file_path:
            数据集文件路径

        :param tokenizer:
            分词器，用于处理 QA 数据

        :param split_name: str
            当前数据集的名称，可选：
            "train"、"valid"、"test"、"visualize"

        :param progress_interval: int
            每处理指定数量的有效记录后输出一次处理进度

        :param read_interval: int
            每读取指定数量的记录后输出一次读取进度

        :param logger:
            日志记录器。
            如果为 None，则使用标准输出打印日志

        :param max_position_embeddings: int
            模型允许的最大输入序列长度

        📋📋📋📋
        请实现该类的构造函数：

        你需要使用json读取jsonl文件
        然后将处理结果储存到一个内部变量中

        请在下方完成你的实现
        """
        raise NotImplementedError("QADataset.__init__ 未实现")


    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]

    def _log_info(self, message):
        if self.logger is None:
            print(message)
        else:
            self.logger.info(message)

class QACollator:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, features):
        """
        将整个samples构建为一个Batch, 并实现MLM数据集的整理

        :param features: list[dict]
            一个 Batch 中的 QA 样本列表。
            每个元素为一个 QA 样本字典，
            由 Dataset 提供

        :return: batch: dict
            一个 Batch 字典，包含模型训练和后续处理所需的数据

        📋📋📋📋
        请实现一个 Batch Collator：
        将输入的多个 QA 样本整理为模型可以直接使用的 Batch 数据，
        并将相关信息组织成字典返回。

        请在下方完成你的实现
        """
        raise NotImplementedError("QACollator.__call__ 未实现")
