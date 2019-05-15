#encoding: utf-8

import contextlib
import inspect
import os
import sys
import traceback


DEBUG = '--debug' in sys.argv


@contextlib.contextmanager
def script_directory():
    '''
    A context manager which allows you to write blocks of code which run within 
    a script's directory. The working directory is restored afterward.
    '''
    cwd = os.getcwd()
    # Frames are: script_directory -> contextlib.contextmanager -> caller
    caller = inspect.getouterframes(inspect.currentframe())[2]
    script_dir = os.path.dirname(os.path.realpath(caller.filename))
    os.chdir(script_dir)
    try:
        yield script_dir
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
