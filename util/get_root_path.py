import os, sys


def get_root_path():
    fn = getattr(sys.modules['__main__'], '__file__')
    root_path = os.path.abspath(os.path.dirname(fn))
    print(root_path)
    return root_path

get_root_path()