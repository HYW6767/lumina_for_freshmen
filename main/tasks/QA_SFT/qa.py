import torch.nn as nn


class QATask(nn.Module):
    def __init__(self, model, loss_fn):
        """
        QA 任务模块的构造函数

        :param model:
            用于 QA 任务的模型

        :param loss_fn:
            QA 任务使用的损失函数。
            如果为 None，则仅进行模型前向计算，不计算损失

        📋📋📋📋
        请实现该类的构造函数：
        完成父类的初始化；
        保存模型和损失函数；

        请在下方完成你的实现
        """
        super(QATask, self).__init__()
        self.model = model
        self.loss_fn = loss_fn

    def forward(self, batch):
        """
        QA 任务的前向传播

        :param batch: dict
            一个 Batch 的输入数据，包含：
            {
                "input_ids": torch.Tensor [B, S]
                    # 输入 Token 的 ID

                "attention_mask": torch.Tensor [B, S]
                    # 输入序列的注意力掩码

                "token_type_ids": torch.Tensor [B, S]
                    # 输入序列中各 Token 对应的类型 ID

                "start_positions": torch.Tensor [B]
                    # 答案起始位置对应的标签

                "end_positions": torch.Tensor [B]
                    # 答案结束位置对应的标签
            }

            其中：
            B 表示 batch size，S 表示序列长度

            当 loss_fn 为 None 时，
            start_positions 和 end_positions 可以不提供

        :return: output_dict: dict
            QA 任务的输出结果：
            {
                "logits": {
                    "start_logits": torch.Tensor [B, S]
                        # 各序列位置作为答案起始位置的预测结果

                    "end_logits": torch.Tensor [B, S]
                        # 各序列位置作为答案结束位置的预测结果
                },

                "loss": torch.Tensor
                    # 当前 Batch 的总体损失。
                    # 当 loss_fn 为 None 时不包含该字段

                "losses": dict
                    # 各项损失的统计信息。
                    # 当 loss_fn 为 None 时不包含该字段

                "details": dict
                    # 起始位置和结束位置对应的损失计算详情。
                    # 当 loss_fn 为 None 时不包含该字段
            }

        📋📋📋📋
        请实现 QA 任务的前向传播方法：
        使用模型完成 QA 前向计算；
        组织 start_logits 和 end_logits；
        当提供损失函数时，根据对应标签完成损失计算；
        整合 QA 任务所需的损失信息；
        返回完整的任务输出结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATask.forward 未实现")
