import torch
import torch.nn as nn

from math import isfinite

class BertEmbedding(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        hidden_size: int,
        max_position_embeddings: int,
        type_vocab_size: int,
        padding_idx: int,
        dropout=0.1,
        layer_norm_eps=1e-12
    ):
        """
        Bert Embedding 层的构造函数

        :param vocab_size: int
            词表大小

        :param hidden_size: int
            隐藏层维度，即每个 token 对应的 embedding 向量维度

        :param max_position_embeddings: int
            模型支持的最大序列长度

        :param type_vocab_size: int
            token 类型的数量

        :param padding_idx: int
            padding token 对应的索引

        :param dropout: float
            Dropout 概率

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        完成该 Embedding 层所需子模块的初始化
        以便下方前向传播使用

        请在下方完成你的实现
        """
        raise NotImplementedError("BertEmbedding.__init__ 未实现")

    def forward(self, input_ids, token_type_ids=None):
        """
        Bert Embedding 层的前向传播

        :param input_ids: torch.Tensor [B, S]
            输入 token 的 ID。
            B 表示 batch size，S 表示序列长度

        :param token_type_ids: torch.Tensor [B, S] or None
            输入序列中各 token 对应的类型 ID。
            如果未提供，则使用默认的 token 类型

        :return: embeddings: torch.Tensor [B, S, H]
            Embedding 层的输出结果。
            B 表示 batch size，S 表示序列长度，
            H 表示 hidden_size

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 input_ids 和 token_type_ids，
        返回符合模型输入要求的 embedding 表示。

        请在下方完成你的实现
        """
        raise NotImplementedError("BertEmbedding.forward 未实现")
