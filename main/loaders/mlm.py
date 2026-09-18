import re
import json
import torch

from math import isfinite
from torch.utils.data import Dataset

def split_text_into_sentences(text):
    """
    将一篇较长的文章拆成句子
    :param text: str
        文章文本text

    :return: sentences: list
        拆分出来的句子

    📋📋📋📋
    此处需要实现一个方法：
    将句子按照标点符号拆分成单句放在一个list中并返回
    请在下方写好你的函数

    """
    raise NotImplementedError("split_text_into_sentences 未实现")

def pack_sentences_into_token_chunks(sentences, tokenizer, max_seq_length):
    """
    把句子tokenize成token
    :param sentences: list[str]
        待处理的句子列表

    :param tokenizer:
        分词器

    :param max_seq_length: int
        最长序列长度

    :return: chunks list
        chunk分块后的列表

    📋📋📋📋
    此处需要实现一个方法：
    将sentences句子列表按照max_seq_length的限制分块成chunk
    最后组装成一个列表返回
    请在下方写好你的函数

    """
    raise NotImplementedError("pack_sentences_into_token_chunks 未实现")

def build_mlm_sample(token_chunk, tokenizer):
    """
    构建用于 MLM 模型输入的样本

    :param token_chunk: list[str]
        单个 chunk 中的 token 列表

    :param tokenizer:
        分词器

    :return: encoded_dict
        一个 dict，包含模型输入所需的信息：
        {
            "input_ids": list[int]
                # 输入序列中各 token 对应的 ID

            "attention_mask": list[int]
                # 输入序列的注意力掩码

            "token_type_ids": list[int]
                # 输入序列中各 token 对应的类型 ID
        }

    📋📋📋📋
    请实现一个 MLM 样本构建方法：
    将输入的 token_chunk 转换为模型可以直接使用的输入格式，
    并将相关信息组织成字典返回。

    请在下方完成你的实现
    """
    raise NotImplementedError("build_mlm_sample 未实现")

class MLMDataset(Dataset):
    def __init__(self, data_file_path, tokenizer, max_seq_length, split_name, progress_interval, read_interval, logger=None):
        """
        MLM的Dataset构造

        :param data_file_path: pathlib.Path
            数据集文件夹路径

        :param tokenizer:
            分词器

        :param max_seq_length: int
            序列最长长度

        :param split_name: str
            数据集名称 train, valid, test, visualize

        :param read_interval: int
            每读取到多少条记录输出一次日志

        :param progress_interval: int
            每处理多少条有效记录输出一次日志。

        :param logger:
            日志记录器

        📋📋📋📋
        请实现该类的构造函数：
        你需要使用json读取jsonl文件
        然后将处理结果储存到一个内部变量中

        请在下方完成该类的构造函数
        """
        raise NotImplementedError("MLMDataset.__init__ 未实现")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]

    def _log_info(self, message):
        if self.logger is None:
            print(message)
        else:
            self.logger.info(message)

class MLMCollator:
    def __init__(self, tokenizer, mlm_prob = 0.15):
        """
        MLM数据集整理器，用于DataLoader

        :param tokenizer:
            分词器

        :param mlm_prob: int
            添加掩码概率

        """
        # 接收参数
        self.tokenizer = tokenizer
        self.mlm_prob = mlm_prob

        if not type(self.mlm_prob) in (int,float) or not 0 < self.mlm_prob < 1 or not isfinite(self.mlm_prob):
            raise ValueError(f"mlm_prob的值必须为(0,1)之间的整数或浮点数喵！，现在是 {self.mlm_prob}")

    def __call__(self, samples):
        """
        将整个samples构建为一个Batch(根据batch_size分batch是后面DataLoader的任务)，并实现MLM数据集的整理
        15%挖空生成labels
        ...

        :param samples:
            一个 dict，包含模型输入所需的信息：
        {
            "input_ids": list[int]
                # 输入序列中各 token 对应的 ID

            "attention_mask": list[int]
                # 输入序列的注意力掩码

            "token_type_ids": list[int]
                # 输入序列中各 token 对应的类型 ID
        }

        :return: mlm_dict:
            一个dict，包含mlm任务模型需要输入的各种信息
        {
            "input_ids": list[int]
                # 输入序列中各 token 对应的 ID

            "attention_mask": list[int]
                # 输入序列的注意力掩码

            "token_type_ids": list[int]
                # 输入序列中各 token 对应的类型 ID

            "labels": list[int]
                # 从数据取出的真实token的id作为真实标签

        }

        📋📋📋📋
        请实现该类的call函数：
        你需要从samples中取出样本
        然后按照比例在合适的地方加上掩码（或随机填充token，或其他操作...）
        并且获取在这些地方的原始token的id作为label
        构造最终的mlm_dict并返回

        请在下方完成该类的call函数
        """
        raise NotImplementedError("MLMCollator.__call__ 未实现")
