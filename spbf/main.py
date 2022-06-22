import click
import os

class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for file in os.listdir(commands_folder):
            if file.endswith(".py") and file.startswith("cmd_"):
                commands.append(file.replace("cmd_","").replace(".py",""))
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"spbf.commands.cmd_{name}", None, None, [cli])
        except ImportError:
            return
        return mod.cli

@click.command(cls=ComplexCLI)
def cli():
    """A Smart Person's Best Friend """
    pass
