from wqp import __version__
import click 

@click.group()
@click.version_option(__version__)
@click.pass_context
def wqp(ctx):
    pass

@wqp.group()
def jobs():
    pass

@jobs.command()
def train():
    pass