# ！？仿佛看到原子弹爆炸？！

**出题人：Master**

**出题人QQ：1531384713**

## Part 2 我也要大战代码？

### Task 1 Lumina

在这个任务中，你需要阅读出题人提供的框架 Lumina，了解项目的整体结构、主要接口以及基本运行方式。

#### Ⅰ. yummy? yaml!

YAML 是一种人类可读的数据序列化格式，经常用于编写项目配置文件。请阅读仓库中的示例配置，并查阅相关资料，回答下列问题。

1. YAML 是什么？在项目中通常拿来做什么？
2. YAML 与 JSON、TOML 等常见配置或数据序列化格式有什么区别？请从语法、可读性、数据类型和适用场景等角度进行比较。
3. 为什么我们要使用yaml？为什么不把这些配置直接写在代码里面？
4. 阅读仓库中的示例 YAML 文件，尤其是 `example_mlm.yaml`，解释各部分配置在实验中的作用。请不要只逐行翻译参数，而应说明它们共同定义了什么实验。
5. 对比 `example_mlm.yaml`、`example_mlm_test.yaml`、`example_mlm_inference.yaml` 和 `example_mlm_visualize.yaml`，说明它们分别对应什么实验模式，并解释它们的配置结构为什么不同。
6. 新建一个用于bert的mlm训练的yaml文件，使用bert-large的模型配置
7. 尝试补齐配置文件中的空白部分

****

#### Ⅱ. 从哪里起飞？从哪里降落？

可能大家做到这里还是一头雾水，那么，我们应该如何运行这个框架呢？请根据仓库的实际结构回答以下问题

1. 找出项目中训练、测试、推理和可视化对应的入口文件 (start_*.py)，并说明各自作用。

2. 根据项目文档或入口代码，写出以下操作对应的终端命令：

   - 使用配置文件进行 MLM 训练；

   - 对训练好的模型进行测试；
   - 使用模型进行推理；
   - 执行可视化；
   - 从已有实验或 checkpoint 恢复训练。

3. 说明终端命令中的配置文件参数有什么作用。
4. 训练、测试、推理和可视化为什么要使用不同的入口，而不是全部写在同一个 Python 文件中？

5. 使用终端命令尝试运行 start_train.py，观察仓库顶层是否生成了新的实验目录。说明该目录的名称由什么决定，并分析其中各个子目录或文件的用途。这一步需要附上**终端运行结果**，并尝试描述一下运行一次训练（单指train）命令执行后发生的事情

6. 一次实验结束后你需要干什么？查看什么文件？
7. 尝试修改一下yaml文件使其故意报错，观察程序是如何处理错误的，说明错误出现的位置，错误信息，以及你是如何定位错误的

****

#### Ⅲ. NotImplementedError

相信大家在做上面的题目的过程中一定遇到了NotImplementedError这样一个报错，其实这里就是大家需要补充编写代码的部分，在接下来几道题中，你需要了解究竟哪些代码是需要自己完成的

*本部分只要求调查和分类，不要求现在实现这些代码；具体实现将在后续 Task 中完成。*

1. 请列出仓库中所有需要补充填写的代码文件路径
2. 按照模块功能将待实现内容进行分类（列出表格）
3. 任选一个待实现模块，说明他的输入，输出，在流程中的作用以及职责

****

### Task 1 附加题

#### Ⅰ. Registry

1. registry是什么？
2. 为什么需要registry？
3. 如果需要添加一个新的模型、任务、Tokenizer 或指标，通常需要在哪些位置进行修改？Registry 在其中承担什么作用？
4. registry有哪些问题？
5. 尝试说出registry机制在该框架下的具体运作方式

****

#### Ⅱ. Parse

1. 你的终端命令是如何被解析的？
2. yaml文件是如何被读取的？
3. yaml配置是如何被规范化并且校验的？
4. 根据源码，尝试将 Parse 过程划分为若干个逻辑阶段，并说明每个阶段的输入、输出和主要作用。划分方式不要求唯一，但需要有代码依据。
5. 如何进行字段的检验？
6. yaml配置填写出现问题应该在哪个阶段被捕获并抛出异常？
7. 为什么不直接使用yaml.safe_load()，而是需要一个如此复杂的parse逻辑？
8. 尝试给出整个parse逻辑的流程图

****

#### Ⅲ. 你的见解

1. 在阅读和使用过程中，你认为当前框架最容易让新用户困惑的地方是什么？
2. 你认为哪些设计比较合理？为什么？
3. 如果只能进行一项改动，你会优先改什么？
4. 请说明这个改动解决了什么问题，以及可能带来的新问题。

****

### Task 2 重温“完形填空”

在这个任务中，你需要完成上方分析的所有待实现模块中mlm任务部分的代码

*可视化链路的可视化方法和 Builder 已提供，无需补写；完成上述 MLM 模型、数据和任务模块后即可直接运行。*

1. 代码文件: main/models/Transformer/tokenizer/tokenizer.py
   - 完成该代码文件中的ExampleTokenizer
   - 说明它的输入输出是什么，以及它在 train、test、inference、visualize 四条链路中分别被谁调用，怎样调用。

2. 代码文件: main/models/Transformer/embedding/embedding.py
   - 完成该代码文件中的BertEmbedding
   - 说明输入 `[B,S]` 如何变成 `[B,S,H]`，几类 embedding 各自解决什么问题，以及 `padding_idx` 的作用是什么。

3. 代码文件: main/models/Transformer/modules/modules.py
   - 完成该代码文件中的所有部分
   - 讲一下你对Q/K/V的理解，说明 Q/K/V 如何切分成多头，`[B,S]` 的 mask 如何扩展并作用于 attention scores，以及 EncoderBlock 中 Attention 子层和 FFN 子层的组织顺序是什么。

4. 代码文件: main/models/Transformer/head/heads.py
   - 完成该代码文件中的BertMLMHead
   - 说明输入 `[B,S,H]` 如何变成 `[B,S,V]`，以及这一部分有什么"特殊机制"。

5. 代码文件: main/models/Transformer/modeling/modeling.py
   - 完成该代码文件中的TinyBertModel和TinyBertForMaskedLM
   - 说明 backbone 输出什么，MLM 模型在 backbone 之上加了什么，两者的职责分工是什么。

6. 代码文件: main/loaders/mlm.py
   - 完成该代码文件中的所有部分
   - 说明 Dataset 输出的单条样本包含哪些字段，Collator 如何做动态 mask，`labels` 中 `-100` 的含义是什么，以及特殊 token 为什么不参与 mask。

7. 代码文件: main/tasks/MLM_PreTrain/mlm.py
   - 完成该代码文件中的MLMTask
   - 说明它从 batch 取出什么送入模型，如何用 `logits[B,S,V]` 和 `labels[B,S]` 计算 loss，以及它返回的字典包含哪些字段，分别被 Trainer、Tester、Visualizer 如何使用。

8. 代码文件: main/Tester/tester.py
   - 完成该代码文件中的所有部分
   - 说明 test 与 train 在数据 shuffle、梯度、checkpoint 加载上有何区别，以及其输入输出是什么。

9.  代码文件: main/Tester/test_runner.py
   - 完成该代码文件中的所有部分
   - 说明它如何串起 task、dataloader、checkpoint、metric_collection、writer，以及其与 `Trainer.fit` 的职责边界在哪里。

10. 代码文件: main/Inference/decoding/decoding.py
    - 完成该代码文件中的TopKSamplingStrategy
    - 说明输入 `logits[V]` 如何变成下一个 token，top-k 和 temperature 分别控制什么，贪心解码是它的什么特例。
11. 代码文件: main/tasks/MLM_PreTrain/inference.py
    - 完成该代码文件中的所有部分
    - 说明 MLM 推理的输入输出与训练时有何不同，其如何循环调用模型和 decoding 策略完成填空，以及其为什么不需要计算 loss。

12. 代码文件: main/metrics/implementations/token_accuracy.py
    - 完成该代码文件中的所有部分
    - 说明其如何用 `ignore_index=-100` 忽略非 mask 位置，其统计的是什么准确率，以及其在 train、valid、test 三个阶段分别由谁调用。

****

### Task 3 模型好像学会了偷懒……

*该部分不要求提出确切有效的改进，考察部分仅限于整个过程，但需要在仓库中体现出你的改进尝试*

1. 代码文件补全后，请先尝试跑通mlm任务的train，test，inference，以及visualize，这一步需要附上运行截图
2. 分析生成的实验结果，你认为你模型预测的效果好吗？你发现了什么问题？给出至少一个你观察到的不良现象截图，并判断模型效果是否符合预期。
3. 请任选一个不良现象进行分析，并说出可能导致这个现象的原因，不要求找出准确的原因，但必须有理有据
4. 针对上述现象，提出并实施至少一种改进，并给出对照实验。
5. 说出你在这个改进过程中的感悟，至少包括一次失败的尝试及其原因分析。

****

### Task 3 附加题

尝试将整个过程写成一篇综述或者小的论文草稿，不要求正式论文格式，但需包含问题描述、复现方式、分析过程、对照实验、结论五个部分，篇幅不限。