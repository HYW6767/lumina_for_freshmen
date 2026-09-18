import torch

from math import isfinite


class Tester:

    def __init__(self, task, test_dataloader, device,
                 metric_collection, metrics_writer, logger=None):
        """
        Tester 测试器的构造函数

        :param task:
            待测试的任务模型

        :param test_dataloader:
            测试数据集对应的 DataLoader

        :param device:
            测试阶段使用的计算设备

        :param metric_collection:
            指标集合，用于记录和计算测试指标

        :param metrics_writer:
            指标结果写入器，用于保存测试结果

        :param logger:
            日志记录器。
            如果为 None，则使用标准输出打印日志

        📋📋📋📋
        请实现该类的构造函数：
        保存测试所需的任务模型、数据加载器和计算设备；
        保存指标集合和指标结果写入器；
        保存日志记录器等相关信息。

        请在下方完成你的实现
        """
        raise NotImplementedError("Tester.__init__ 未实现")

    def _transfer_batch_device(self, batch):
        """
        将 Batch 中的数据迁移到指定计算设备

        :param batch: dict
            一个 Batch 的数据。
            Batch 中可能包含 Tensor 类型和其他类型的数据

        :return: new_batch: dict
            迁移到指定设备后的 Batch 数据

        📋📋📋📋
        请实现 Batch 设备迁移方法：
        将 Batch 中需要进行设备迁移的数据转换到当前 Tester
        指定的计算设备，并保持 Batch 的数据结构。

        请在下方完成你的实现
        """
        raise NotImplementedError("Tester._transfer_batch_device 未实现")

    def _log_info(self, message):
        if self.logger is None:
            print(message)
        else:
            self.logger.info(message)

    def evaluate(self):
        """
        执行完整的模型测试流程

        :return: summary_dict: dict
            测试结果汇总信息：
            {
                "completed_batches": int
                    # 实际完成测试的 Batch 数量

                "last_loss": float
                    # 最后一个已完成 Batch 的损失

                "avg_loss": float
                    # 测试过程中的平均损失

                "losses": dict
                    # 各项损失的统计结果。
                    # 每项包含：
                    # {
                    #     "avg_raw": float
                    #         # 对应损失的平均原始值
                    #
                    #     "avg_weighted_loss": float
                    #         # 对应损失的平均加权值
                    #
                    #     "weight": float
                    #         # 当前损失对应的权重
                    # }

                "test_metrics": dict
                    # 指标集合计算得到的测试指标
            }

        📋📋📋📋
        请实现模型测试方法：
        完成测试阶段所需的状态初始化；
        将任务模型设置为测试状态，并配置计算设备；
        对测试数据进行批次级别的推理；
        检查并统计模型输出中的损失信息；
        更新测试指标；
        计算测试阶段的汇总损失和指标；
        保存测试结果；
        输出必要的测试日志；
        返回完整的测试结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("Tester.evaluate 未实现")
