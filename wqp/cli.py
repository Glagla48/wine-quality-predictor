from wqp import __version__
from wqp.workflow import model_training_workflow

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
@click.option(
            '--data-path',
            default='http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',
            help='train the model with the given path or a default path'
            )
def train(data_path:str):
    model_training_workflow(data_path=data_path)