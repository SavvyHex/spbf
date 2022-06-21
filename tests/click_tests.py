import click

@click.group()      # Used to group similar commands together
def cli():
    pass

@cli.command()
@click.argument("name")         # Basically a normal argument in a method
def hello(name):
    print(f"Hello {name}")

@cli.command()
@click.option("--n", type=int, default=1)       # Optional parameters
def ha(n):
    for x in range(n):
        print("ha")

if __name__ == "__main__":
    cli()
