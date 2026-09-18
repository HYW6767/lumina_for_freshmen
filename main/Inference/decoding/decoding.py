import torch

from math import isfinite


class TopKSamplingStrategy:
    """
    Top-K 采样策略。
    请完成下面的构造函数和解码方法。
    """

    def __init__(self, top_k=5):
        """
        Top-K 采样策略的构造函数

        :param top_k: int
            保留的候选 token 数量

        📋📋📋📋
        请在下方实现该类的构造函数
        """
        raise NotImplementedError("TopKSamplingStrategy.__init__ 未实现")

    def decode(self, logits):
        """
        Top-K 采样策略的解码主方法

        :param logits: torch.Tensor [S]
            模型对于当前预测位置输出的 logits，
            S 表示词表大小(vocab_size)

        :return: summary_dict
            一个 dict，包含本次解码的相关信息：
            {
                "top_logits": top_logits,
                    # Top-K 候选 token 对应的 logits

                "top_token_ids": top_token_ids,
                    # Top-K 候选 token 的 ID

                "sampling_scores": sampling_scores,
                    # Top-K 候选 token 对应的采样概率

                "selected_candidate_index": sampled_candidate_index,
                    # 被采样出的 token 在 Top-K 候选列表中的索引

                "selected_token_id": sampled_token_id,
                    # 最终采样得到的 token ID
            }

        📋📋📋📋
        请在下方实现该类的 decode 主方法
        """
        raise NotImplementedError("TopKSamplingStrategy.decode 未实现")


class QASpanTopKDecodingStrategy:
    """
    QA 任务 Span 解码的 Top-K 策略。
    请完成下面的构造函数和解码方法。
    """

    def __init__(self, max_answer_length=30, n_best_size=20):
        """
        QA 任务 Span 解码 Top-K 策略的构造函数

        :param max_answer_length: int
            答案 Span 允许的最大 token 长度

        :param n_best_size: int
            保留的候选 token 数量

        📋📋📋📋
        请在下方实现该类的构造函数
        """
        raise NotImplementedError("QASpanTopKDecodingStrategy.__init__ 未实现")

    def decode(
        self,
        start_logits,
        end_logits,
        token_type_ids,
        attention_mask,
        offset_mappings,
        context,
    ):
        """
        QA 任务 Span 解码的 Top-K 策略主方法

        :param start_logits: torch.Tensor [S]
            每个 token 作为答案起始位置的预测 logits

        :param end_logits: torch.Tensor [S]
            每个 token 作为答案结束位置的预测 logits

        :param token_type_ids: torch.Tensor [S]
            输入序列中每个 token 的类型标识，
            用于区分输入中的不同文本片段

        :param attention_mask: torch.Tensor [S]
            输入序列中每个 token 的有效性掩码

        :param offset_mappings: list [S]
            每个 token 在原始 context 中的字符位置映射，
            每个元素的格式为 (start_char, end_char)

        :param context: str
            原始上下文文本

        :return: best_candidate
            一个 dict，包含最终预测答案的相关信息：
            {
                "start_index": start_index,
                    # 答案起始位置对应的 token 索引

                "end_index": end_index,
                    # 答案结束位置对应的 token 索引

                "start_char": start_char,
                    # 答案在 context 中的起始字符位置

                "end_char": end_char,
                    # 答案在 context 中的结束字符位置

                "answer": answer,
                    # 从 context 中截取出的答案文本

                "score": span_score,
                    # 当前答案 Span 的得分

                "start_logit": start_logit,
                    # 答案起始位置对应的 logit

                "end_logit": end_logit,
                    # 答案结束位置对应的 logit
            }

        📋📋📋📋
        请在下方实现该类的 decode 主方法
        """
        raise NotImplementedError("QASpanTopKDecodingStrategy.decode 未实现")
