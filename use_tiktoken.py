import getopt
import re
import sys
from typing import List
import requests
import tiktoken
from tiktoken.load import load_tiktoken_bpe

def load_encoding(**models):
    models['mergeable_ranks'] = load_tiktoken_bpe(models['mergeable_ranks'])
    enc = tiktoken.Encoding(**models)
    return enc

def get_encoding(model_file: str, special_tokens: List[str]):
    matched = re.search(r"(\w+\.\w+)$", model_file)
    if matched:
        file_name = matched[1].split(".")[0]
    if 'http://' in model_file or 'https://' in model_file:
        vocab_size = len(requests.get(model_file).text.strip().split('\n'))
    else:
        vocab_size = len(open(model_file).readlines())
    special_size = len(special_tokens)
    special_dict = {}
    special_index = vocab_size
    for special_token in special_tokens:
        special_dict[special_token] = special_index
        special_index += 1

    constructor = {
        "name": file_name,
        "explicit_n_vocab": vocab_size + special_size,
        "pat_str": r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""",
        "mergeable_ranks": model_file,
        "special_tokens": special_dict,
    }
    print(constructor)
    enc = load_encoding(**constructor)
    return enc

if __name__=="__main__":
    argv = sys.argv[1:]
    try:
        options, args = getopt.getopt(argv, "m:s:", ["model =", "special_tokens ="])
    except:
        print("Error Message ")

    special_tokens = []
    for name, value in options:
        if name in ['-m', '--model']:
            model_file = value
        if name in ['-s', '--special_tokens']:
            special_tokens = value.split(":")

    enc = get_encoding(model_file, special_tokens)
    ts = enc.encode("First, you know Caius Marcius is chief enemy to the people.", allowed_special="all")
    print(ts)
    print(enc.decode(ts))
    ts = enc.encode("道德经 :持⽽盈之，不如其已；揣⽽锐之，不可⻓保。⾦⽟满堂，莫之能守；富贵⽽骄，⾃遗其咎。功遂身退天之道。", allowed_special="all")
    print(ts)
    print(enc.decode(ts))
    # for line in open('/Users/tsinghuaboy/projects/Open-GPT/tokenizer/shakespeare_input.txt'):
    #     print(enc.encode(line, allowed_special="all"))

