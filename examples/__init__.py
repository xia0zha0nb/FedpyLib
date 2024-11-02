from ....FedpyLib import __init__ as father
from examples import *

__all__ = [
    "colorstring",
    "completion",
    "extra",
    "linecharts",
    "timer",
    "random"
]

if __name__ == '__main__':
    print("This is the __init__.py file of the examples folder.")
    noexample = father.__all__ - __all__
    if noexample:
        print(f"These modules don't have examples: {noexample}.")
    else:
        print("All modules have examples.")