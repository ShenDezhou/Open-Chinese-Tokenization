import getopt
import sys
from educational import *
from tiktoken.load import dump_tiktoken_bpe

gpt2_pattern = (
        r"""'s|'t|'re|'ve|'m|'ll|'d| ?[\p{L}]+| ?[\p{N}]+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    )

if __name__=="__main__":
    argv = sys.argv[1:]
    try:
        options, args = getopt.getopt(argv, "i:n:o:", ["input =", "vocab_size =", "output ="])
    except:
        print("Error Message ")

    for name, value in options:
        if name in ['-i', '--input']:
            input_file = value
        if name in ['-n', '--vocab_size']:
            vocab_size = int(value)
        if name in ['-o', '--output']:
            output_file = value

    with open(input_file, "r") as f:
        data = f.read()

    enc = SimpleBytePairEncoding.train(data, vocab_size=vocab_size, pat_str=gpt2_pattern)

    dump_tiktoken_bpe(enc.mergeable_ranks, output_file)
