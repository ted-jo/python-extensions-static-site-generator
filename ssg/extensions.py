import sys
import importlib
from importlib import Path, import_module

def load_module(directory, name):
    sys.path.insert(0, directory)
    import_module(name)
    sys.path.pop(0)

def load_directory(directory):
    for path in directory.Path.rglob("*.py"):
        load_module(directory.as_posix(), path.stem)