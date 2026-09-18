import torch
import torch.nn as nn

class MLMTask(nn.Module):
    def __init__(self, model, loss_fn):
        """
        MLM 任务模块的构造函数

        :param model:
            用于 MLM 任务的模型

        :param loss_fn:
            MLM 任务使用的损失函数。
            如果为 None，则仅进行模型前向计算，不计算损失

        📋📋📋📋
        请实现该类的构造函数：
        完成父类的初始化；
        保存模型和损失函数；

        请在下方完成你的实现
        """
        super(MLMTask, self).__init__()
        # 接收参数
        self.model = model
        self.loss_fn = loss_fn

    def forward(self, batch):
        """
        MLM 任务的前向传播

        :param batch: dict
            一个 Batch 的输入数据，包含：
            {
                "input_ids": torch.Tensor [B, S]
                    # 输入 Token 的 ID

                "attention_mask": torch.Tensor [B, S]
                    # 输入序列的注意力掩码

                "token_type_ids": torch.Tensor [B, S]
                    # 输入序列中各 Token 对应的类型 ID

                "labels": torch.Tensor [B, S]
                    # MLM 任务对应的标签。
                    # 当 loss_fn 不为 None 时需要提供
            }

            B 表示 batch size，S 表示序列长度

        :return: output_dict: dict
            模型前向计算及损失计算得到的结果：
            {
                "logits": torch.Tensor [B, S, V]
                    # 模型对各位置 Token 的预测结果

                "loss": torch.Tensor
                    # 当前 Batch 的总体损失。
                    # 当 loss_fn 为 None 时不包含该字段

                "losses": dict or other
                    # 损失函数返回的其他损失信息。
                    # 当 loss_fn 为 None 时不包含该字段
            }

            V 表示词表大小

        📋📋📋📋
        请实现 MLM 任务的前向传播方法：
        使用模型完成 MLM 前向计算；
        组织模型输出；
        当提供损失函数时，完成损失计算并保存相关结果；
        返回完整的任务输出结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("MLMTask.forward 未实现")

