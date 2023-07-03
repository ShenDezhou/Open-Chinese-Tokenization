# Open Tokenization for Chinese

本项目分享了一些常用领域的中文tiktoken模型。

# 如何使用模型

本地模型加载，命令行示例：`python use_tiktoken.py -m e1k_base/e1k_base.tiktoken -s '<|endoftext|>'`

网络模型加载，命令行示例：`python use_tiktoken.py -m https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/e1k_base.ticktoken -s '<|endoftext|>'`

代码示例：
```python
from use_tiktoken import get_encoding
enc = get_encoding('e1k_base/e1k_base.tiktoken', ['<|endoftext|>'])
tokens = enc.encode("First, you know Caius Marcius is chief enemy to the people.", allowed_special="all")
```

或者

```python
from use_tiktoken import get_encoding
enc = get_encoding('https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/e1k_base.ticktoken', ['<|endoftext|>'])
tokens = enc.encode("First, you know Caius Marcius is chief enemy to the people.", allowed_special="all")
```

# 如何训练

示例:`python train_tiktoken.py -i corpus.txt -n 1000 -o e1k_base.tiktoken`


# 分词下载

| 数据集    | owner      | model         | 语言 | 词表数  |
|--------|------------|---------------|----|------|
| 多语种语料  | OpenAI     | [p50k_base]   | multi | 50k  |
| 多语种语料  | OpenAI     | [r50k_base]   | multi | 50k  |
| 多语种语料  | OpenAI     | [cl100k_base] | multi | 100k |
| 戏剧     | Brian Shen | [e1k_base]    | en | 1k   | 
| 小说     | Brian Shen | [c1k_base]    | cn | 1k   | 
| 小说     | Brian Shen | [c10k_base]   | cn | 10k  | 
| 小说     | Brian Shen | [c20k_base]   | cn | 20k  | 
| 小说     | Brian Shen | [c80k_base]   | cn | 80k  | 

[p50k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/p50k_base.tiktoken
[r50k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/r50k_base.tiktoken
[cl100k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/cl100k_base.tiktoken
[e1k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/e1k_base.ticktoken
[c1k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/c1k_base.tiktoken
[c10k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/c10k_base.tiktoken
[c20k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/c20k_base.tiktoken
[c80k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/c80k_base.tiktoken

# 压缩率对比

我们在中文对话语料上对比上述分词器的压缩率，给定一个含8167句中文对话语料，其分词token数对比如下：

> 压缩率，描述压缩文本符号的效果，是文本压缩后的token数大小与压缩前的大小之比。压缩率越小，说明分词器对文本编码效率越高。
> 这里我们选择p50k_base作为基线，这是GPT2的分词器，使用较为广泛。

| model    | token数 | 压缩率      |
|----------|----|----------|
|p50k_base | 758757 | 100%     |
|r50k_base | 758757 | 100%     |
|cl100k_base | 467011 | 61.5494% |
|e1k_base  | 1084408 | 142.919% | 
|c1k_base  | 414715 | 54.6571% |
|c10k_base | 257976 | 33.9998% | 
|c20k_base | 237925 | 31.3572% |
|c80k_base | 209451 | 27.6045% |

从上述表格可见，GPT3.5/4的压缩率与GPT2相比提升约39%，GPT3.5/4的词表数比GPT2增加了一倍，但压缩率显著提升。
我们在中文语料上训练的c1k分词器压缩率比GPT4提升约7%,c10k提升约27%,c20k提升约30%,c80k提升约34%。
我们在英文语料上训练的e1k分词器压缩率下降约43%。

由此可见，在中文领域重新训练分词器有利于压缩token长度，仅用GPT4编码器1%的词表数，取得了编码效率优势。
词表数更小意味着给定相同参数的后续网络条件下，由于有更小的嵌入层，整体网络参数量更少，因此具有一定的计算速度优势。
因此，中文分词器c[1,10,20,80]k在中文领域下与GPT3.5/4通用编码器更具编码、计算速度优势。

统计代码在[analysis_models.py](analysis_models.py)，读者可以自行在其他中文语料进行测评验证。

## 关注我们
欢迎关注知乎专栏号。

[深度学习兴趣小组](https://www.zhihu.com/column/thuil)


## 问题反馈 & 贡献
如有问题，请在GitHub Issue中提交。  
我们没有运营，鼓励网友互相帮助解决问题。  
如果发现实现上的问题或愿意共同建设该项目，请提交Pull Request。

