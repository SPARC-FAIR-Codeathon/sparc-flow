import click
import json


@click.command()
@click.argument('name', type=str)
def hash_users_name(name):
    click.echo(json.dumps({'answer': str(hash(name))}))


if __name__ == '__main__':
    hash_users_name()