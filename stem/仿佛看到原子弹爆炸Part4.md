# ！？仿佛看到原子弹爆炸？！

## Part 4 我们需要再深入些

*这一部分不需要使用出题人提供的github仓库了，只需写好文档，附上必要的截图，并在docs文件夹中存放好相关代码文件即可*

### Task 1 transformers

在前面的任务中，我们已经学习并实现过 Transformer、BERT 等模型，也接触过完整的深度学习训练流程。

在实际的大模型开发中，我们通常不会重复实现这些基础模型，而是使用成熟的开源模型库。

本任务将学习目前常用的开源模型库之一——Hugging Face Transformers。

本任务不要求重新学习 Transformer 或 BERT 的基础原理，而是希望你通过实际使用 Transformers，了解一个成熟的大模型库通常提供哪些能力，以及如何使用这些能力完成实际任务。

## 任务

1. 首先尝试在你的虚拟环境中安装好transformers库

2. Transformers 是什么？它主要解决什么问题？除了模型本身之外，它还提供了哪些与模型开发相关的功能？

3. 安装 Transformers，并尝试运行一个官方提供的预训练模型。

   完成一次从：

   `文本 → Tokenizer → Model → Output`

   的完整流程。

   记录并解释整个过程中产生的主要数据。

4. 了解 Transformers 中常见的几个核心接口，例如：

   - `AutoTokenizer`
   - `AutoConfig`
   - `AutoModel`
   - `AutoModelForSequenceClassification`
   - `AutoModelForTokenClassification`
   - `AutoModelForQuestionAnswering`
   - `AutoModelForCausalLM`
   - `AutoModelForMaskedLM`

   说明这些接口分别解决什么问题，并思考为什么需要针对不同任务提供不同的模型接口。

5. 尝试使用 `AutoTokenizer` 完成文本处理，并观察 Tokenizer 的以下行为：

   - 文本如何转换为 Token；
   - Token 如何转换为 Token ID；
   - Padding 和 Truncation 是什么；
   - `attention_mask` 有什么作用；
   - 如何将 Token ID 转换回文本。

6. 尝试使用 `from_pretrained()` 加载一个已经训练好的模型。

   说明：

   - `from_pretrained()` 加载了什么；
   - 模型结构如何确定；
   - 模型参数从哪里获得；
   - Config、Model 和 Tokenizer 三者之间是什么关系。

7. Transformers 中有大量针对不同任务封装好的模型。

   请至少选择两种不同类型的任务进行实验，例如：

   - 文本分类
   - Token 分类
   - 问答
   - Masked Language Modeling
   - Causal Language Modeling
   - 文本生成

   对比它们的输入、输出以及模型结构上的区别。

8. 尝试使用一个 Causal Language Model 完成文本生成。

   调查并尝试理解 `generate()` 的基本使用方式，并观察以下参数对生成结果的影响：

   - `max_new_tokens`
   - `do_sample`
   - `temperature`
   - `top_k`
   - `top_p`

9. 尝试查看你所使用模型的 Config，并理解其中几个重要参数的含义。

   思考：为什么使用同一个 Transformers 接口，却可以加载不同规模、不同结构的模型？

10. 尝试完成一次模型的保存与重新加载。

    验证重新加载后的模型是否能够得到与保存前一致的结果，并了解 Transformers 中模型、Tokenizer 和 Config 通常是如何进行保存的。

11. 在完成上述实验后，尝试独立完成一个小型任务：

    **使用 Transformers 选择一个你感兴趣的预训练模型，完成一个实际的 NLP 任务。**

    要求说明：

    - 为什么选择这个模型；
    - 模型适合解决什么问题；
    - 输入是什么；
    - 输出是什么；
    - 使用了 Transformers 中哪些组件；
    - 最终实验结果如何。

****

### Task 2 大模型前沿

1. 你眼中的“大模型”发展到了什么阶段？

从你目前所学的 Transformer、BERT、GPT 等模型出发，尝试梳理大模型的发展过程。

不要求完整复述历史，可以选择你认为重要的几个阶段或关键技术，并说明：

- 它解决了什么问题？
- 为什么会出现？
- 相比之前的方法有什么变化？
- 它对后续大模型的发展产生了什么影响？

2. 选择至少三个近年来的大模型技术方向进行调研

可以从以下方向中选择，也可以选择其他你感兴趣的方向：

- Scaling Law
- MoE（Mixture of Experts）
- 长上下文
- 多模态大模型
- Reasoning / 推理模型
- Test-time Compute
- RLHF / DPO / RL 等后训练方法
- Synthetic Data
- Distillation
- Speculative Decoding
- KV Cache
- Quantization
- Flash Attention
- Agent
- Tool Use
- RAG
- World Model
- Embodied AI
- 其他你认为重要的方向

对于每个方向，尝试回答：

- 它是什么？
- 为什么需要它？
- 它主要解决什么问题？
- 基本原理是什么？
- 它对大模型的训练、推理或应用有什么影响？
- 当前有哪些具有代表性的模型、论文或开源项目？

3. 选择一个你感兴趣的“大模型”

可以选择一个目前较为知名的开源或闭源模型。

尝试从以下方面进行分析：

- 模型规模
- 模型架构
- 上下文长度
- 训练方式
- 后训练方式
- 是否支持多模态
- 是否具备推理能力
- 是否支持工具调用
- 是否开源，以及开源到了什么程度

不要求所有信息都能够找到，但需要区分官方公开的信息、论文中给出的信息、社区推测以及你自己的理解。

4. 一个有趣的问题：大模型究竟是在“变聪明”，还是在“使用更多计算”？

结合近年来 Reasoning Model、Test-time Compute 等方向进行调研。

尝试讨论：

- 什么是 Test-time Compute？
- 为什么增加推理阶段的计算量可能提高模型表现？
- 这种方法与传统的扩大模型参数量有什么区别？
- “训练时计算”和“推理时计算”分别承担什么作用？
- 这种趋势可能会给未来的大模型带来什么变化？

5. 从“模型”走向“系统”

我们之前学习的大部分内容，都围绕：

> 输入 → 模型 → 输出

但现在的大模型应用越来越像一个完整系统。

请选择 Agent、RAG、Tool Use、Memory、Multimodal 等方向中的一个或多个进行调研，并思考：

> 当一个大模型开始调用工具、访问外部知识、保存信息或者与环境交互之后，它还是一个“模型”吗？

结合你自己的理解进行讨论。

6. 最后，选择一个你认为未来值得关注的问题

不要简单回答“未来大模型会越来越强”。

请选择一个具体问题，例如：

- 模型规模是否还会继续增长？
- 推理计算是否会成为新的 Scaling 方向？
- MoE 是否会成为主流架构？
- 多模态模型会如何发展？
- Agent 是否会成为大模型的重要应用形式？
- 大模型是否会越来越依赖合成数据？
- 训练和推理的成本如何继续下降？
- 开源模型与闭源模型会如何发展？

给出你的观点，并使用资料支持你的分析。