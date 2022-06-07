#Maria Williams 6/6/22
#using click to interact with a pre-trained ML model

import click
import pickle
import torch
import transformers
from transformers import GPT2Tokenizer

@click.command()
def hello():
    #open model, instantiate tokenizer, and print welcome message
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    click.echo('Let me finish your thought! Type "hush" to stop chatting.')

    while True:
        #prompt for input until imput is "hush"
        call = click.prompt('What is on your mind?')
        if call=="hush":
            break

        #retrieve output from model
        input_ids = tokenizer.encode(call, return_tensors='pt')
        output = model.generate(input_ids, max_length = 30, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        output = tokenizer.decode(output[0])

        #remove extra returns and the original input
        output = output.replace('\n',' ')
        output = output.replace(call,'')
        output = output[1:]
        output = output.strip()

        #trim output to first full sentence
        if output.find('.') > 0:
            firstind = output.find('.') 
            firstind += 1
            answer = output[0: firstind]
        elif output.find('?') > 0:
            firstind = output.find('?') 
            firstind += 1
            answer = output[0: firstind]
        else:
            answer = output

        #print out response
        click.echo(f'{answer}')
    click.echo("Goodbye")

if __name__ == '__main__':
    hello()