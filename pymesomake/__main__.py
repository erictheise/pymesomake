import click
from .pymesomake import mesosticize


@click.command()
@click.option('--sourcefile', prompt='file containing source text')
@click.option('--mesostring', prompt='Mesostic spine, surrounded by quotes')
@click.option('--rule', prompt='rule, 50 or 100', default=50)
def click_wrapper(sourcefile, mesostring, rule):
    """A command line wrapper for PyMesomake."""
    with open(sourcefile, 'r') as f:
        sourcetext = f.read()
    print(mesosticize(sourcetext, mesostring, rule))


if __name__ == '__main__':
  click_wrapper()
