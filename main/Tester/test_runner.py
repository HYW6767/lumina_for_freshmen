import pathlib

from Trainer.checkpoint import load_checkpoint
from Tester.tester import Tester


def _load_task_checkpoint(task, checkpoint_path):
    """
    加载任务模型的 Checkpoint

    :param task:
        待恢复参数的任务模型

    :param checkpoint_path:
        Checkpoint 文件路径

    :return: checkpoint: dict
        加载得到的 Checkpoint 数据，
        包含模型任务状态及其他检查点信息

    请实现 Checkpoint 加载方法：
    处理并规范 Checkpoint 文件路径；
    加载 Checkpoint 数据；
    对 Checkpoint 的格式和内容进行必要的合法性检查；
    将 Checkpoint 中的任务状态恢复到 task；
    返回加载得到的 Checkpoint 数据。

    请在下方完成你的实现
    """
    raise NotImplementedError("_load_task_checkpoint 未实现")

def _log_info(logger, message):
    if logger is None:
        print(message)
    else:
        logger.info(message)

def run_test(task, test_dataloader, checkpoint_path, device,
             metric_collection, metrics_writer, logger=None):
    """
    执行模型测试流程

    :param task:
        待测试的任务模型

    :param test_dataloader:
        测试数据集对应的 DataLoader

    :param checkpoint_path:
        测试阶段优先使用的 Checkpoint 文件路径

    :param device:
        测试阶段使用的计算设备

    :param metric_collection:
        指标集合，用于计算测试结果

    :param metrics_writer:
        指标结果写入器，用于保存测试结果

    :param logger:
        日志记录器。
        如果为 None，则使用标准输出打印日志

    :return: summary_dict: dict
        测试流程的汇总结果：
        {
            "checkpoint_path":
                # 实际用于测试的 Checkpoint 路径

            "test_summary":
                # Tester 返回的测试结果汇总信息
        }

    📋📋📋📋
    请实现测试流程：
    对测试所需的输入参数进行必要的处理；
    尝试加载可用的模型 Checkpoint；
    记录 Checkpoint 加载过程中的相关信息；
    创建并配置 Tester；
    执行测试并获取测试结果；
    整理测试结果并记录测试完成信息；
    返回完整的测试结果。

    请在下方完成你的实现
    """
    raise NotImplementedError("run_test 未实现")
