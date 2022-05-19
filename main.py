#Maria Williams 5/19/22
#playing around with click
#referencing https://zetcode.com/python/click/

import click

@click.command()
#argument: pass by adding after command
#@click.argument('hw', default='world')

#option: pass by adding after tag
@click.option("--name", prompt="Your name", help="Provide your name")
@click.option('--lang', default="english", help="type english or spanish")

def hello(name, lang):
    if lang=="english":
        click.echo(f'Hello {name}')
    elif lang=="spanish":
        click.echo(f'Hola {name}')
    else:
        click.echo('Language not recognized')

if __name__ == '__main__':
    hello()