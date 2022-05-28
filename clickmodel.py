#Maria Williams 5/27/22
#playing around with click
#see if I can get a model working

import click
import pickle
import torch
import transformers
from transformers import GPT2Tokenizer


@click.command()
@click.option('--call', prompt="Say Something", help="Provide some text that the model can use to generate more text")
#@click.option("--say", prompt="Your name", help="Provide your name")
def hello(call):
    #model = pickle.load(open('model.pkl', 'rb'))
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    input_ids = tokenizer.encode(call, return_tensors='pt')
    output = model.generate(input_ids, max_length = 20, num_return_sequences=1)
    output = tokenizer.decode(output[0])


    click.echo(f'{output}')

if __name__ == '__main__':
    hello()