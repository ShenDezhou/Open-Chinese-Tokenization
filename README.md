# Open Tokenization for Chinese

本项目分享了一些常用领域的tiktoken模型。

# 如何使用模型

命令行示例：`python use_tiktoken.py -m e1k_base/e1k_base.tiktoken -s '<|endoftext|>'`

命令行示例：`python use_tiktoken.py -m https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/e1k_base.ticktoken -s '<|endoftext|>'`

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

| 数据集 | owner      | model        | 语言 | 词表数    |
|-----|------------|--------------|----|--------|
| 戏剧  | Brian Shen | [e1k_base]   | en | 1000   | 
| 小说  | Brian Shen | [c1k_base]   | cn | 1000   | 
| 小说  | Brian Shen | [c10k_base]  | cn | 10000  | 
| 小说  | Brian Shen | [c100k_base] | cn | 100000 | 

[e1k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/e1k_base.ticktoken
[c1k_base]: https://transformers-models.obs.cn-north-4.myhuaweicloud.com/gpt/tokenizer/c1k_base.tiktoken
[c10k_base]:
[c100k_base]:

## 关注我们
欢迎关注知乎专栏号。

[深度学习兴趣小组](https://www.zhihu.com/column/thuil)


## 问题反馈 & 贡献
如有问题，请在GitHub Issue中提交。  
我们没有运营，鼓励网友互相帮助解决问题。  
如果发现实现上的问题或愿意共同建设该项目，请提交Pull Request。

