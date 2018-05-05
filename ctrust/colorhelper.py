from __future__ import print_function

import sys
from termcolor import cprint, colored


def print_error(message):
    return cprint(message, 'red', attrs=['bold'], file=sys.stderr)


def print_info(*args):
    assert args
    if len(args) > 1:
        print(args[0], info(' '.join((args[1:]))))
    else:
        cprint(args[0], 'cyan')


def print_success(message):
    return cprint(message, 'green', attrs=['bold'])


def print_warn(message):
    return cprint(message, 'yellow', attrs=['bold'], file=sys.stderr)


def info(message):
    return colored(message, 'cyan')


def warning(message):
    return colored(message, 'yellow')

def success(message):
    return colored(message, 'green', attrs=['bold'])
