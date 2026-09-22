# ！？仿佛看到原子弹爆炸？！

## Part 3 过家家就到此为止吧

*遊びはここまでだ*

### Task 1 抽取式QA

在之前的招新题或者任务中，你已经了解到了什么是模型的预训练，什么是模型的微调，在这个Part中，我们将使用上个part训练好的mlm模型，进行一系列微调来完成抽取式QA任务，在此之前，请查找资料并回答下列基础问题：

1. 什么是抽取式QA？它和gpt回答你的问题有什么区别？
2. 为什么本项目中的 BERT 只做抽取式 QA，而不是像 GPT 那样直接生成回答？
3. MLM任务和QA任务有哪些不同？请从输入输出，模型结构，张量维度几个方面回答
4. QA 微调时，MLM 预训练权重是如何被加载的？backbone 和 task head 分别发生了什么？
5. QA任务会用到什么指标？为什么用这些指标？
6. 什么是offset_mapping？为什么需要这个数据
7. 模型输出是如何映射到原文中的？
8. 除了上述任务提到的，你认为mlm和qa还有哪些不同点？
9. 请编写qa任务所需要的yaml配置文件，并比较这些配置文件与mlm的yaml配置文件有什么不同点

### Task 2 搞半天还是要自己写

在这个任务中，你需要完成之前分析中所有待实现模块中qa任务部分的代码

*可视化链路的可视化方法和 Builder 已提供，无需补写；完成上述 QA 模型、数据和任务模块后即可直接运行。*

1. 代码文件: main/models/Transformer/tokenizer/tokenizer.py
   - 请完成该代码文件中的QATokenizer
   - 说明其与 ExampleTokenizer 的关系，以及带 offset 的分词结果如何支撑答案位置映射。

2. 代码文件: main/models/Transformer/head/heads.py
   - 请完成该代码文件中的BertQAHead
   - 说明其输入输出形状，以及它与 BertMLMHead 在任务语义上的区别。

3. 代码文件: main/models/Transformer/modeling/modeling.py
   - 请完成该代码文件中的TinyBertForQuestionAnswering
   - 说明 backbone 与 QA head 的分工。

4.  代码文件: main/loaders/qa.py
   - 请完成该代码文件中的所有部分
   - 说明 QA 样本的字段构成

5. 代码文件: main/tasks/QA_SFT/qa.py
   - 请完成该代码文件中的QATask
   - 说明从 batch 取出什么、送入模型后如何计算 loss、返回什么。

6. 代码文件: main/Inference/decoding/decoding.py
   - 请完成该代码文件中的QASpanTopKDecodingStrategy
   - 说明其输入输出是什么，以及它与 MLM 解码策略的区别。

7. 代码文件：main/tasks/QA_SFT/inference.py

      \- 请完成该代码文件中的 QAInference

      \- 说明其如何将模型输出还原为原文答案文本。

8. 代码文件: main/metrics/implementations/character_f1.py

   - 请完成该代码文件中的所有部分
   - 说明其统计对象是什么。

9. 代码文件: main/metrics/implementations/exact_match.py

   - 请完成该代码文件中的所有部分

   - 说明其统计对象是什么，以及它与 character_f1 的区别。

****

### Task 3 机器休息我学习

这一部分与上一个part的task3要求一样

*该部分不要求提出确切有效的改进，考察部分仅限于整个过程，但需要在仓库中体现出你的改进尝试*

1. 代码文件补全后，请先尝试跑通qa任务的train，test，inference，以及visualize，这一步需要附上运行截图
2. 分析生成的实验结果，你认为你模型预测的效果好吗？你发现了什么问题？给出至少一个你观察到的不良现象截图，并判断模型效果是否符合预期。
3. 请任选一个不良现象进行分析，并说出可能导致这个现象的原因，不要求找出准确的原因，但必须有理有据
4. 针对上述现象，提出并实施至少一种改进，并给出对照实验。
5. 说出你在这个改进过程中的感悟，至少包括一次失败的尝试及其原因分析。

****

### Task 3 附加题

尝试将整个过程写成一篇综述或者小的论文草稿，不要求正式论文格式，但需包含问题描述、复现方式、分析过程、对照实验、结论五个部分，篇幅不限。

## Part 3 BOSS附加题 电磁场的天气是红灯的变种

尝试使用 Lumina 框架制作一个自己的 gpt 并打通四条链路，要求与前两个任务一致，但没有直接给出待实现模块与数据集，需要自己找到解决方法
