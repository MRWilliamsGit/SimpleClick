#Maria Williams 5/27/22
#playing around with click
#see if I can get a model working

import click
from transformers import pipeline

@click.command()
@click.argument('call', prompt="Say Something:", help="Provide some text that the model can use to generate more text")
#@click.option("--say", prompt="Your name", help="Provide your name")
def hello(call):
    robot = pipeline('text-generation', model = "gpt2")
    ans = robot(call, max_length=20, num_return_sequences=1)[0]
    click.echo(f'{ans}')

if __name__ == '__main__':
    hello()