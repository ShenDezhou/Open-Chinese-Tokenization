import json
import pandas
from use_tiktoken import get_encoding

enc_dic = {
    'e1k': 'e1k_base/e1k_base.tiktoken',
    'c1k': 'c1k_base/c1k_base.tiktoken',
    'p50k': 'p50k_base/p50k_base.tiktoken',
    'r50k': 'r50k_base/r50k_base.tiktoken',
    'cl100k': 'cl100k_base/cl100k_base.tiktoken'
}
with open('xianjian_test.json') as f:
    testsets = json.load(f)['test']
    testsets = [[line[0].replace(" ", "", 10**2), line[1].replace(" ", "", 10**2)] for line in testsets]

    result_dic = {}
    for key in enc_dic.keys():
        enc = get_encoding(enc_dic[key], ["<|endoftext|>"])
        enc_lines = []
        for line in testsets:
            enc_lines.append([enc.encode(line[0]),enc.encode(line[1])])
        enc_len = [[len(line[0]),len(line[1])] for line in enc_lines]
        result_dic[key] = enc_len

    with open("enc_len.json","w") as fw:
        json.dump(result_dic, fw)

#统计各个分词器文本编码字数
    df = pandas.read_json("enc_len.json")
    len_result = {}
    sum_result = {}
    for col in df.columns:
        len_result[col] = df[col].agg('sum')
        sum_result[col] = pandas.Series(len_result[col]).agg('sum')
    print("="*40)
    print(sum_result)
    print("=" * 40)

