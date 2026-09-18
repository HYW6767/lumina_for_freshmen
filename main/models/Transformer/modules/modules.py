import torch
import torch.nn as nn

from math import sqrt, isfinite

def _extend_attention_mask(attention_mask):
    """
    扩展 Attention Mask

    :param attention_mask: torch.Tensor [B, S]
        输入序列的注意力掩码。
        B 表示 batch size，S 表示序列长度

    :return: extended_attention_mask: torch.Tensor [B, 1, 1, S]
        扩展后的注意力掩码

    📋📋📋📋
    请实现一个 Attention Mask 扩展方法：
    将输入的 attention_mask 转换为模型后续计算所需的格式。

    请在下方完成你的实现
    """
    raise NotImplementedError("_extend_attention_mask 未实现")

class MultiHeadSelfAttention(nn.Module):
    def __init__(self, hidden_size, num_heads, attention_dropout=0.1):
        """
        多头自注意力模块的构造函数

        :param hidden_size: int
            隐藏层维度

        :param num_heads: int
            多头注意力的头数

        :param attention_dropout: float
            Attention 权重的 Dropout 概率

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成多头自注意力模块所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("MultiHeadSelfAttention.__init__ 未实现")

    def forward(self, hidden_states, attention_mask=None):
        """
        多头自注意力模块的前向传播

        :param hidden_states: torch.Tensor [B, S, H]
            输入的隐藏状态。
            B 表示 batch size，S 表示序列长度，
            H 表示 hidden_size

        :param attention_mask: torch.Tensor [B, S] or None
            输入序列的注意力掩码

        :return: output: torch.Tensor [B, S, H]
            多头自注意力模块的输出结果

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 hidden_states 和 attention_mask，
        返回多头自注意力模块的输出结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("MultiHeadSelfAttention.forward 未实现")

    def _split_heads(self, tensor, batch_size, seq_length):
        """
        拆分多头表示

        :param tensor: torch.Tensor [B, S, H]
            待处理的隐藏状态

        :param batch_size: int
            当前批次的大小

        :param seq_length: int
            当前序列的长度

        :return: tensor: torch.Tensor [B, N, S, D]
            多头表示。
            N 表示 num_heads，D 表示每个注意力头的维度

        📋📋📋📋
        请实现多头表示的维度转换方法，
        返回符合多头注意力计算要求的张量。

        请在下方完成你的实现
        """
        raise NotImplementedError("MultiHeadSelfAttention._split_heads 未实现")


class AttentionOutput(nn.Module):
    def __init__(self, hidden_size, dropout=0.1, layer_norm_eps=1e-12):
        """
        Attention 输出模块的构造函数

        :param hidden_size: int
            隐藏层维度

        :param dropout: float
            Dropout 概率

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成该模块所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("AttentionOutput.__init__ 未实现")

    def forward(self, attention_output, residual_input):
        """
        Attention 输出模块的前向传播

        :param attention_output: torch.Tensor [B, S, H]
            Attention 模块产生的输出

        :param residual_input: torch.Tensor [B, S, H]
            残差连接所需的输入

        :return: output: torch.Tensor [B, S, H]
            Attention 输出模块的最终结果

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 attention_output 和 residual_input，
        返回该模块的输出结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("AttentionOutput.forward 未实现")


class FeedForwardNetwork(nn.Module):
    def __init__(self, hidden_size, intermediate_size, dropout=0.1):
        """
        Feed Forward Network 的构造函数

        :param hidden_size: int
            隐藏层维度

        :param intermediate_size: int
            前馈网络中间层维度

        :param dropout: float
            Dropout 概率

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成前馈网络所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("FeedForwardNetwork.__init__ 未实现")

    def forward(self, hidden_states):
        """
        Feed Forward Network 的前向传播

        :param hidden_states: torch.Tensor [B, S, H]
            输入的隐藏状态。
            B 表示 batch size，S 表示序列长度，
            H 表示 hidden_size

        :return: output: torch.Tensor [B, S, H]
            前馈网络的输出结果

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 hidden_states，
        返回前馈网络的输出结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("FeedForwardNetwork.forward 未实现")


class FeedForwardOutput(nn.Module):
    def __init__(self, hidden_size, layer_norm_eps=1e-12):
        """
        Feed Forward Network 输出模块的构造函数

        :param hidden_size: int
            隐藏层维度

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成该模块所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("FeedForwardOutput.__init__ 未实现")

    def forward(self, ffn_output, residual_input):
        """
        Feed Forward Network 输出模块的前向传播

        :param ffn_output: torch.Tensor [B, S, H]
            前馈网络产生的输出

        :param residual_input: torch.Tensor [B, S, H]
            残差连接所需的输入

        :return: output: torch.Tensor [B, S, H]
            Feed Forward Network 输出模块的最终结果

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 ffn_output 和 residual_input，
        返回该模块的输出结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("FeedForwardOutput.forward 未实现")


class EncoderBlock(nn.Module):
    def __init__(
        self,
        hidden_size,
        num_heads,
        intermediate_size,
        attention_dropout=0.1,
        hidden_dropout=0.1,
        layer_norm_eps=1e-12
    ):
        """
        Encoder Block 的构造函数

        :param hidden_size: int
            隐藏层维度

        :param num_heads: int
            多头注意力的头数

        :param intermediate_size: int
            前馈网络中间层维度

        :param attention_dropout: float
            Attention 模块的 Dropout 概率

        :param hidden_dropout: float
            隐藏层的 Dropout 概率

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成 Encoder Block 所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("EncoderBlock.__init__ 未实现")

    def forward(self, hidden_states, attention_mask=None):
        """
        Encoder Block 的前向传播

        :param hidden_states: torch.Tensor [B, S, H]
            输入的隐藏状态

        :param attention_mask: torch.Tensor [B, S] or None
            输入序列的注意力掩码

        :return: output: torch.Tensor [B, S, H]
            Encoder Block 的输出结果

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 hidden_states 和 attention_mask，
        返回 Encoder Block 的输出结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("EncoderBlock.forward 未实现")


class Encoder(nn.Module):
    def __init__(
        self,
        hidden_size,
        num_heads,
        intermediate_size,
        num_layers,
        attention_dropout=0.1,
        hidden_dropout=0.1,
        layer_norm_eps=1e-12
    ):
        """
        Encoder 模块的构造函数

        :param hidden_size: int
            隐藏层维度

        :param num_heads: int
            多头注意力的头数

        :param intermediate_size: int
            前馈网络中间层维度

        :param num_layers: int
            Encoder Block 的数量

        :param attention_dropout: float
            Attention 模块的 Dropout 概率

        :param hidden_dropout: float
            隐藏层的 Dropout 概率

        :param layer_norm_eps: float
            LayerNorm 使用的数值稳定性参数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的模型参数；
        完成 Encoder 所需子模块的初始化。

        请在下方完成你的实现
        """
        raise NotImplementedError("Encoder.__init__ 未实现")

    def forward(self, hidden_states, attention_mask=None):
        """
        Encoder 模块的前向传播

        :param hidden_states: torch.Tensor [B, S, H]
            输入的隐藏状态

        :param attention_mask: torch.Tensor [B, S] or None
            输入序列的注意力掩码

        :return: hidden_states: torch.Tensor [B, S, H]
            Encoder 模块输出的隐藏状态

        📋📋📋📋
        请实现该类的前向传播方法：
        根据输入的 hidden_states 和 attention_mask，
        返回经过 Encoder 模块处理后的隐藏状态。

        请在下方完成你的实现
        """
        raise NotImplementedError("Encoder.forward 未实现")
