#Maria Williams 5/19/22
#playing around with click
#referencing https://zetcode.com/python/click/

import click

@click.command()
#argument: pass by adding after command
#@click.argument('name', default='guest')
#option: pass by adding after tag
@click.option('--lang', default="english", help="type english or spanish")
@click.option("--name", prompt="Your name", help="Provide your name")
def hello(lang, name):
    if lang=="english":
        click.echo(f'Hello {name}')
    elif lang=="spanish":
        click.echo(f'Hola {name}')
    else:
        click.echo('Language not recognized')

if __name__ == '__main__':
    hello()