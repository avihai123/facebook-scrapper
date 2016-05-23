# import click
# @click.command()
# @click.option('--count', default=None, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     if count is None:
#         raise click.BadParameter('If a value is provided it needs to be the '
#                                  'value "wat".', param_hint=['--foo'])
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
#
# @click.command()
# @click.option('--add_page', nargs=2, type=click.Tuple([unicode, int]))
# def putitem(item):
#     click.echo('name=%s id=%d' % item)
#
# if __name__ == '__main__':
#     hello()