import torch
import torch.nn as nn

from math import isfinite

class BertMLMHead(nn.Module):
    def __init__(self, hidden_size, vocab_size, layer_norm_eps=1e-12):
        """
        BERT MLM 任务头的构造函数

        :param hidden_size: int
            隐藏层维度

        :param vocab_size: int
            词表大小

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成 MLM 任务头所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("BertMLMHead.__init__ 未实现")

    def forward(self, hidden_states):
        """
        BERT MLM 任务头的前向传播

        :param hidden_states: torch.Tensor [B, S, H]
            BERT 编码器输出的隐藏状态。
            B 表示 batch size，S 表示序列长度，
            H 表示 hidden_size

        :return: logits: torch.Tensor [B, S, V]
            每个位置对应词表中各 token 的预测 logits。
            B 表示 batch size，S 表示序列长度，
            V 表示 vocab_size

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 hidden_states，
        返回 MLM 任务所需的预测结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("BertMLMHead.forward 未实现")


class BertQAHead(nn.Module):
    def __init__(self, hidden_size):
        """
        BERT QA 任务头的构造函数

        :param hidden_size: int
            隐藏层维度

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成 QA 任务头所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("BertQAHead.__init__ 未实现")

    def forward(self, hidden_states):
        """
        BERT QA 任务头的前向传播

        :param hidden_states: torch.Tensor [B, S, H]
            BERT 编码器输出的隐藏状态。
            B 表示 batch size，S 表示序列长度，
            H 表示 hidden_size

        :return: logits_dict: dict
            一个 dict，包含 QA 任务所需的预测 logits：
            {
                "start_logits": torch.Tensor [B, S],
                    # 每个位置对应的起始位置 logits
                "end_logits": torch.Tensor [B, S]
                    # 每个位置对应的结束位置 logits
            }

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 hidden_states，
        返回 QA 任务所需的预测结果，
        并将相关结果组织成字典返回。

        请在下方完成你的实现
        """
        raise NotImplementedError("BertQAHead.forward 未实现")
