#encoding: utf-8

import contextlib
import traceback
import os
import sys


DEBUG = '--debug' in sys.argv


@contextlib.contextmanager
def script_directory():
    '''
    A context manager which allows you to write blocks of code which run within 
    this script's directory. The working directory is restored afterward.
    '''
    cwd = os.getcwd()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    try:
        yield
    finally:
        os.chdir(cwd)


def raise_hell(f):
    '''
    Traceback displaying decorator for callbacks whose exceptions get expunged
    '''

    import traceback
    def wrapper(*a, **kw):
        try: return f(*a, **kw)
        except Exception:
            traceback.print_exc(limit=-1)
            raise
    return wrapper


__all__ = [
    'DEBUG',
    'raise_hell',
    'script_directory',
]
