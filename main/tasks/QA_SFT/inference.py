import torch

class QAInference:
    def __init__(self, model, tokenizer, decoding_strategy, max_position_embeddings, doc_stride):
        """
        QA 推理器的构造函数

        :param model:
            用于 QA 任务推理的模型

        :param tokenizer:
            分词器，用于将 question 和 context 编码为模型输入，
            并提供 Token 与原始文本之间的位置信息

        :param decoding_strategy:
            QA 解码策略，用于根据模型输出生成答案候选结果。
            应提供可调用的 decode 方法

        :param max_position_embeddings: int
            模型允许的最大输入序列长度

        :param doc_stride: int
            处理较长文本时，相邻输入窗口之间的重叠长度

        📋📋📋📋
        请实现该类的构造函数：
        完成成员变量的初始化；
        保存模型、分词器、解码策略及序列长度等信息。

        请在下方完成你的实现
        """
        raise NotImplementedError("QAInference.__init__ 未实现")

    def infer(self, input_data):
        """
        执行 QA 推理

        :param input_data: dict
            QA 推理所需的输入数据，包含：
            {
                "question": str
                    # 待回答的问题

                "context": str
                    # 用于回答问题的上下文文本
            }

        :return: result: dict
            当前 QA 推理的最终结果。
            在候选答案信息的基础上包含：
            {
                "question": str
                    # 原始问题

                "context": str
                    # 原始上下文

                "answer": str
                    # 最终预测得到的答案

                "result_text": str
                    # 最终推理结果文本

                "score": float
                    # 最终答案对应的评分

                "window_index": int
                    # 最终答案所在的输入窗口索引

                "window_count": int
                    # 本次推理生成的输入窗口数量
            }

            以及解码策略返回的其他候选答案信息。

        📋📋📋📋
        请实现 QA 推理方法：
        对输入数据进行必要的合法性检查；
        将 question 和 context 转换为模型所需的输入格式；
        完成各输入窗口的模型推理；
        根据解码策略生成各窗口对应的答案候选结果；
        汇总所有窗口的候选答案；
        得到最终的 QA 推理结果；
        将最终结果组织成字典返回。

        请在下方完成你的实现
        """
        raise NotImplementedError("QAInference.infer 未实现")

