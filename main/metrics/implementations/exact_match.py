from metrics.core.base import Metric
from metrics.process.inputs import process_predictions_references

class ExactMatch(Metric):
    def __init__(self):
        super().__init__()
        self.exact_matched = 0
        self.count = 0

    def process(self, **context):
        process_dict = process_predictions_references(**context)
        return process_dict

    def update(self, **context):
        """
        更新 Exact Match 指标的统计结果

        :param context:
            当前批次的预测结果和参考答案等相关信息。
            具体数据格式由 process_predictions_references 负责处理。

        📋📋📋📋
        请实现该方法：
        根据当前批次的 predictions 和 references，
        更新 Exact Match 指标所需的统计信息。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExactMatch.update 未实现")

    def compute(self):
        """
        计算最终的 Exact Match 指标

        :return: summary_dict
            一个 dict，包含最终的指标结果：
            {
                "exact_match": float
                    # Exact Match 指标
            }

        📋📋📋📋
        请实现该方法：
        根据当前累计的统计信息计算最终指标，
        并将结果组织成字典返回。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExactMatch.compute 未实现")

    def reset(self):
        self.exact_matched = 0
        self.count = 0

    def output_fields(self):
        return ["exact_match"]
