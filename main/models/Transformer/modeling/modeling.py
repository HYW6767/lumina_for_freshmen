import torch.nn as nn

from ..embedding.embedding import BertEmbedding
from ..modules.modules import Encoder
from ..head.heads import BertMLMHead, BertQAHead


class TinyBertModel(nn.Module):
    def __init__(
        self,
        vocab_size,
        hidden_size,
        max_position_embeddings,
        type_vocab_size,
        padding_idx,
        num_heads,
        intermediate_size,
        num_layers,
        embedding_dropout=0.1,
        attention_dropout=0.1,
        hidden_dropout=0.1,
        layer_norm_eps=1e-12,
    ):
        """
        TinyBERT 基础模型的构造函数

        :param vocab_size: int
            词表大小

        :param hidden_size: int
            隐藏层维度

        :param max_position_embeddings: int
            模型支持的最大序列长度

        :param type_vocab_size: int
            token 类型的数量

        :param padding_idx: int
            padding token 对应的索引

        :param num_heads: int
            多头自注意力机制的头数

        :param intermediate_size: int
            Encoder 中间层的维度

        :param num_layers: int
            Encoder 层数

        :param embedding_dropout: float
            Embedding 层的 Dropout 概率

        :param attention_dropout: float
            Attention 层的 Dropout 概率

        :param hidden_dropout: float
            隐藏层的 Dropout 概率

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成模型所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("TinyBertModel.__init__ 未实现")

    def forward(self, input_ids, attention_mask=None, token_type_ids=None):
        """
        TinyBERT 基础模型的前向传播

        :param input_ids: torch.Tensor [B, S]
            输入 token 的 ID。
            B 表示 batch size，S 表示序列长度

        :param attention_mask: torch.Tensor [B, S] or None
            注意力掩码，用于表示输入序列中各位置的有效性

        :param token_type_ids: torch.Tensor [B, S] or None
            输入序列中各 token 对应的类型 ID

        :return: hidden_states: torch.Tensor [B, S, H]
            模型输出的隐藏状态。
            B 表示 batch size，S 表示序列长度，
            H 表示 hidden_size

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 input_ids、attention_mask 和 token_type_ids，
        返回模型的隐藏状态表示。

        请在下方完成你的实现
        """
        raise NotImplementedError("TinyBertModel.forward 未实现")


class TinyBertForMaskedLM(nn.Module):
    def __init__(
        self,
        vocab_size,
        hidden_size,
        max_position_embeddings,
        type_vocab_size,
        padding_idx,
        num_heads,
        intermediate_size,
        num_layers,
        embedding_dropout=0.1,
        attention_dropout=0.1,
        hidden_dropout=0.1,
        layer_norm_eps=1e-12,
    ):
        """
        TinyBERT MLM 模型的构造函数

        :param vocab_size: int
            词表大小

        :param hidden_size: int
            隐藏层维度

        :param max_position_embeddings: int
            模型支持的最大序列长度

        :param type_vocab_size: int
            token 类型的数量

        :param padding_idx: int
            padding token 对应的索引

        :param num_heads: int
            多头自注意力机制的头数

        :param intermediate_size: int
            Encoder 中间层的维度

        :param num_layers: int
            Encoder 层数

        :param embedding_dropout: float
            Embedding 层的 Dropout 概率

        :param attention_dropout: float
            Attention 层的 Dropout 概率

        :param hidden_dropout: float
            隐藏层的 Dropout 概率

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成基础模型和 MLM 任务头的初始化；
        完成模型参数之间必要的共享设置

        请在下方完成你的实现
        """
        raise NotImplementedError("TinyBertForMaskedLM.__init__ 未实现")

    def forward(self, input_ids, attention_mask=None, token_type_ids=None):
        """
        TinyBERT MLM 模型的前向传播

        :param input_ids: torch.Tensor [B, S]
            输入 token 的 ID。
            B 表示 batch size，S 表示序列长度

        :param attention_mask: torch.Tensor [B, S] or None
            注意力掩码，用于表示输入序列中各位置的有效性

        :param token_type_ids: torch.Tensor [B, S] or None
            输入序列中各 token 对应的类型 ID

        :return: logits: torch.Tensor [B, S, V]
            MLM 任务的预测 logits。
            B 表示 batch size，S 表示序列长度，
            V 表示 vocab_size

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入数据完成模型前向计算，
        返回 MLM 任务所需的预测结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("TinyBertForMaskedLM.forward 未实现")


class TinyBertForQuestionAnswering(nn.Module):
    def __init__(
        self,
        vocab_size,
        hidden_size,
        max_position_embeddings,
        type_vocab_size,
        padding_idx,
        num_heads,
        intermediate_size,
        num_layers,
        embedding_dropout=0.1,
        attention_dropout=0.1,
        hidden_dropout=0.1,
        layer_norm_eps=1e-12,
    ):
        """
        TinyBERT QA 模型的构造函数

        :param vocab_size: int
            词表大小

        :param hidden_size: int
            隐藏层维度

        :param max_position_embeddings: int
            模型支持的最大序列长度

        :param type_vocab_size: int
            token 类型的数量

        :param padding_idx: int
            padding token 对应的索引

        :param num_heads: int
            多头自注意力机制的头数

        :param intermediate_size: int
            Encoder 中间层的维度

        :param num_layers: int
            Encoder 层数

        :param embedding_dropout: float
            Embedding 层的 Dropout 概率

        :param attention_dropout: float
            Attention 层的 Dropout 概率

        :param hidden_dropout: float
            隐藏层的 Dropout 概率

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成基础模型和 QA 任务头的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("TinyBertForQuestionAnswering.__init__ 未实现")

    def forward(self, input_ids, attention_mask=None, token_type_ids=None):
        """
        TinyBERT QA 模型的前向传播

        :param input_ids: torch.Tensor [B, S]
            输入 token 的 ID。
            B 表示 batch size，S 表示序列长度

        :param attention_mask: torch.Tensor [B, S] or None
            注意力掩码，用于表示输入序列中各位置的有效性

        :param token_type_ids: torch.Tensor [B, S] or None
            输入序列中各 token 对应的类型 ID

        :return: logits_dict: dict
            一个 dict，包含 QA 任务所需的预测结果：
            {
                "start_logits": torch.Tensor [B, S]
                    # 起始位置对应的 logits
                "end_logits": torch.Tensor [B, S]
                    # 结束位置对应的 logits
            }

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入数据完成模型前向计算，
        返回 QA 任务所需的预测结果，
        并将相关结果组织成字典返回。

        请在下方完成你的实现
        """
        raise NotImplementedError("TinyBertForQuestionAnswering.forward 未实现")
