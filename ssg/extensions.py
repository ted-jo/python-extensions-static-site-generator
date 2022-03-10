import sys
import importlib
from importlib import Path, import_module

def load_module(directory, name):
    sys.path.insert(0, directory)
    import_module(name)
    sys.path.pop(0)