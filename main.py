#Maria Williams 5/19/22
#playing around with Click
#referencing https://zetcode.com/python/click/

import click

@click.command()
#argument: pass by adding after command
#@click.argument('name', default='guest')
#option: pass by adding after tag
@click.option('--lang', default="english", help="type english or spanish")
@click.option("--name", prompt="Your name", help="Provide your name")
def hello(l, name):
    if l=="english":
        click.echo(f'Hello {name}')
    elif l=="spanish":
        click.echo(f'Hola {name}')
    else:
        click.echo('Language not recognized')

if __name__ == '__main__':
    hello()