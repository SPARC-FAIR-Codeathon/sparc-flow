import click
import json


@click.command()
@click.argument('name', type=str)
def greet(name):
    click.echo(json.dumps({'answer': f"Hello {name}!"}))


if __name__ == '__main__':
    greet()