# ！？仿佛看到原子弹爆炸？！



**出题人：Master**

**出题人QQ：1531384713**

****

***“爱，死亡，与机器人”***

[大家做到这里都很不容易呀，不妨看个视频放松一下](https://www.bilibili.com/video/BV1P1vfB8EVj/?spm_id_from=333.337.search-card.all.click&vd_source=93f6a1cd4c5da79afaf3cdd42be31dfe)

![neuro](../img/neuro.png)

***“Do I feel love?”***

***"Am I real?"***

***"Do I matter to you?"***



**<span style="font-family: 'Segoe Script';">
"Matter Eternal, Cyber Immortal" </span>**

****



## 导言

现在是一个AI的时代，近几年出现的GPT，Claude Code，Gemini，deepseek，豆包都是大语言模型（简称大模型，LLM），不少人都想进入AI领域，相信很多同学都是为了学习大模型才选择ML方向的，那么什么是大模型，他的发展与历史又怎样呢，如何学习大模型呢，大模型领域又涉及到哪些知识呢？不妨通过以下题目一起学习吧！

****

## ⚠做题前必读⚠

- 请**star**并fork该仓库: [master-yshj/lumina_for_freshmen: 凌睿工作室二轮招新题目](https://github.com/master-yshj/lumina_for_freshmen)，接下来的任务都将围绕该仓库进行
- 最终题解请以github链接的方式提交
- 该题题量很大，难度很高，建议先保证能做完前面的题目再来挑战该题（如果很想尝试，那也建议做完上一道transformer的题目再来挑战）
- 若多次提交，请在提交时注明第几次提交，做了什么修改，添加了什么新东西

****

## Part 1 来点basic！

### Task 1 仅仅是准备工作

可能大伙并不知道这个仓库是干嘛的，没关系，我们先做好以下准备工作！

1. 将你fork的仓库拉取到本地

2. 在main目录创建docs文件夹，这里用于放置**文字类题目解答的md文档**（文档需要分类放置，文档结构类似于下方结构）

   ```
   ├── Part1
   │   ├── Task1
   │   └── Task2
   └── Part2
       └── Task1
   ```

   **✍🏻要求✍🏻: 该步需要附上tree命令在"main目录"的运行结果**

3. 严肃阅读README文档！！！！然后尝试在wsl中使用miniconda创建指定python环境，使用conda list列出你的环境列表，

   **✍🏻要求✍🏻: 该步需要附上python环境以及conda list命令运行结果截图**

4. 进入 ./main/dataset 数据集，找到里面所有的download.py，并运行，将数据集下载到本地（chinese_wiki约19.7GB，cmrc2018约52MB）

   **✍🏻要求✍🏻: 该步需要附上download成功运行的截图**

****

### Task 1 附加题

尝试阅读一下整个文件夹，说出你对这个仓库的理解（其实挺希望大家锐评一下）

****

### Task 2 我怎么还要写文档口牙

这个任务我们会先了解一下大模型最最最最最最基础的知识，请查找资料回答以下问题

相关资料(只需寻找自己需要的信息即可)：

- [Transformer论文逐段精读【论文精读】_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1pu411o7BE?spm_id_from=333.788.videopod.sections&vd_source=93f6a1cd4c5da79afaf3cdd42be31dfe)
- [[1706.03762v6\] Attention Is All You Need](https://arxiv.org/abs/1706.03762v6)

1. 谈谈你对大模型的理解，或者说，对大模型有什么印象？大模型的“大”到底在哪里？
2. 我们天天使用的豆包，deepseek，千问，到底算严格意义上的大模型吗？
3. 到底啥是token？他跟大模型啥关系？为啥现在的大模型都用token计费？
4. tokenizer又是啥？他是模型吗？他是干啥的？
5. embedding又是啥？
6. 你认为大模型和我们招新之前涉及到的模型有啥区别？
7. 什么是Encoder？什么是Decoder？什么是Transformer？
8. 从架构层面谈谈你对Transformer的理解
9. 列举出一些经典的大模型/模型族（至少三个），并谈谈他们各自的特点，优缺，开源情况，应用场景等
10. 什么是下游任务？什么是任务头？什么是backbone？

****

### TASK 2 附加题

1. 模型的参数与显存有什么关系？如何计算一个模型的参数量以及显存占用情况？
2. 计算精度是啥？对模型训练有什么影响？如何选择计算精度？
3. 什么是 Agent？它与大模型是什么关系？大模型与 Agent 在一个任务中分别承担什么职责？为什么单纯依靠一次 LLM 调用难以完成某些复杂任务？

### TASK 3 初识BERT

在前面的任务和招新题中，我们已经认识到了一个模型究竟是如何完成训练的，也知道了关于大模型最基础的一部分知识，在这个任务中，我们来认识一个经典的大模型——BERT

