import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("expression")
def solve(expression):
    click.echo(eval(expression))

if __name__ == "__main__":
    cli()
