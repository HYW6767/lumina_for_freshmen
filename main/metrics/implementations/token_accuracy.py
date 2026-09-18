import torch

from metrics.core.base import Metric
from metrics.process.inputs import process_logits_labels

class TokenAccuracy(Metric):
    def __init__(self, ignore_index=-100):
        if not type(ignore_index) is int:
            raise ValueError(f"ignore_index必须为整型的喵! 现在的type: {type(ignore_index)}")
        super().__init__()
        self.ignore_index = ignore_index

        self.reset()

    def process(self, **context):
        process_dict = process_logits_labels(**context)
        return process_dict

    def update(self, **context):
        """
        更新 Token Accuracy 指标的统计结果

        :param context:
            当前批次的模型输出和标签等相关信息。
            具体数据格式由 process_logits_labels 负责处理。

            其中：
            - labels: torch.Tensor [B, S]
                当前批次的 token 标签
            - logits: torch.Tensor [B, S, V]
                当前批次的 token 分类输出，
                B 表示 batch size，S 表示序列长度，V 表示类别数量

        📋📋📋📋
        请实现该方法：
        根据当前批次的 logits 和 labels，
        更新 Token Accuracy 指标所需的统计信息。

        请在下方完成你的实现
        """
        raise NotImplementedError("TokenAccuracy.update 未实现")

    def compute(self):
        """
        计算最终的 Token Accuracy 指标

        :return: summary_dict
            一个 dict，包含最终的指标结果：
            {
                "token_accuracy": float
                    # Token Accuracy 指标
            }

        📋📋📋📋
        请实现该方法：
        根据当前累计的统计信息计算最终指标，
        并将结果组织成字典返回。

        请在下方完成你的实现
        """
        raise NotImplementedError("TokenAccuracy.compute 未实现")

    def reset(self):
        self.correct_count = 0
        self.total_count = 0

    def output_fields(self):
        return ["token_accuracy"]