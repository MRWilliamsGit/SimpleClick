# Maria Williams
# 6/10/22

from transformers import GPT2Tokenizer
from clickmodel import lmodel, chat


def test_run():
    m = lmodel()
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    result = chat(m, tokenizer, "hi")
    assert len(result) > 0
