#Maria Williams 6/4/22
#using click to call a model

import click
import pickle
import torch
import transformers
from transformers import GPT2Tokenizer

@click.command()
def hello():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    q="no"
    click.echo('Let me finish your thought! Type "hush" to stop chatting.')

    while True:
        call = click.prompt('What is on your mind?')
        if call=="hush":
            break
        input_ids = tokenizer.encode(call, return_tensors='pt')
        output = model.generate(input_ids, max_length = 20, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        output = tokenizer.decode(output[0])
        click.echo(f'{output}')
    click.echo("Goodbye")

if __name__ == '__main__':
    hello()